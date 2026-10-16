# agent.py -- ATS CV Reviewer Agent
# This file NEVER changes when tools are added/removed.
# It connects to server.py, loads whatever tools are registered there,
# and runs a LangGraph ReAct loop.

import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # prevent broken CUDA DLL on Windows

import asyncio
import traceback
import threading

from langchain_ollama import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from gui import build_gui  # GUI is in its own file

# Config
MODEL      = "mistral:7b"
SERVER     = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server.py")
PYTHON_EXE = "C:/Users/Mustapha/AppData/Local/Programs/Python/Python311/python.exe"


# LangGraph agent
async def run_agent(cv_path: str, job_desc: str, on_chunk):
    """
    Connect to the MCP server, discover tools automatically,
    run the ReAct agent and stream results via on_chunk().
    """
    server_params = StdioServerParameters(command=PYTHON_EXE, args=[SERVER])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Discover ALL tools registered in server.py (agent never changes)
            tools = await load_mcp_tools(session)
            on_chunk(f"[MCP] Tools available: {[t.name for t in tools]}\n\n")

            llm   = ChatOllama(model=MODEL, temperature=0)
            agent = create_react_agent(llm, tools)

            prompt = (
                f"You are an expert ATS (Applicant Tracking System) CV reviewer.\n"
                f"CV file: {cv_path}\n\n"
                f"Job Description:\n{job_desc}\n\n"
                f"Instructions:\n"
                f"1. Use read_cv_pdf to extract the CV text.\n"
                f"2. Use score_cv to score it against the job description.\n"
                f"3. Write a clear, actionable ATS report with score, matched/missing "
                f"keywords, and improvement tips."
            )

            async for event in agent.astream(
                {"messages": [{"role": "user", "content": prompt}]},
                stream_mode="updates",
            ):
                for node, data in event.items():
                    for msg in data.get("messages", []):
                        kind = type(msg).__name__
                        if kind == "AIMessage":
                            if msg.content:
                                on_chunk(f"Agent:\n{msg.content}\n\n")
                            for tc in getattr(msg, "tool_calls", []):
                                on_chunk(f">> Calling: {tc['name']}\n")
                        elif kind == "ToolMessage":
                            # content can be a str or a list of {type, text} blocks
                            raw = msg.content
                            if isinstance(raw, list):
                                raw = " ".join(
                                    item.get("text", str(item)) if isinstance(item, dict)
                                    else str(item)
                                    for item in raw
                                )
                            preview = raw[:300] + ("..." if len(raw) > 300 else "")
                            on_chunk(f"<< Result ({msg.name}):\n{preview}\n\n")


# Bridge between GUI button and async agent
def start_review(cv_path, job_desc, output_widget, btn, status_var):
    import tkinter as tk

    if not cv_path:
        output_widget.config(state="normal")
        output_widget.insert(tk.END, "Please select a CV PDF file first.\n")
        output_widget.config(state="disabled")
        return

    output_widget.config(state="normal")
    output_widget.delete("1.0", tk.END)
    output_widget.config(state="disabled")
    btn.config(state="disabled")
    status_var.set("Reviewing...")

    def append(text):
        output_widget.config(state="normal")
        output_widget.insert(tk.END, text)
        output_widget.see(tk.END)
        output_widget.config(state="disabled")

    def unwrap(exc):
        # Recursively unwrap ExceptionGroup (from MCP TaskGroup)
        if hasattr(exc, "exceptions") and exc.exceptions:
            return unwrap(exc.exceptions[0])
        return f"{type(exc).__name__}: {exc}"

    def run():
        try:
            asyncio.run(run_agent(cv_path, job_desc, append))
            status_var.set("Done!")
        except BaseException as e:
            traceback.print_exc()
            append(f"\nError:\n{unwrap(e)}\n")
            status_var.set("Error")
        finally:
            btn.config(state="normal")

    threading.Thread(target=run, daemon=True).start()


if __name__ == "__main__":
    build_gui(start_review)