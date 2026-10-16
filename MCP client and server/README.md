# ATS CV Reviewer — MCP Tutorial

A **minimal** MCP server + agent example for an ATS (Applicant Tracking System) CV reviewer.
Built with **MCP (FastMCP)** + **Mistral:7b via Ollama**.

```
server.py   ← MCP Server  (2 tools)
agent.py    ← MCP Client  (LLM agent that uses the tools)
```

---

## Architecture

```
agent.py  (MCP Client)
   │
   │  spawns as subprocess (stdio transport)
   ▼
server.py (MCP Server)
   ├── Tool: read_cv_pdf   → extracts text from PDF
   └── Tool: score_cv      → keyword-match score vs job description
```

The agent uses **Mistral:7b** (running locally in Ollama) to decide which tools to call and produces a final human-friendly ATS report.

---

## Prerequisites

1. **Python 3.11+**
2. **Ollama** with Mistral:7b pulled:
   ```bash
   ollama pull mistral:7b
   ollama serve          # starts Ollama on http://localhost:11434
   ```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python agent.py path/to/cv.pdf "Job description text here"
```

**Example:**
```bash
python agent.py my_cv.pdf "We need a Python developer with FastAPI, SQL, Docker and REST API experience."
```

---

## MCP Server Tools

| Tool | Args | Returns |
|------|------|---------|
| `read_cv_pdf` | `pdf_path: str` | Extracted CV text |
| `score_cv` | `cv_text: str`, `job_description: str` | JSON report with score & keywords |

---

## How it works (step by step)

1. `agent.py` spawns `server.py` as a subprocess via **stdio transport**
2. The agent sends a prompt to **Mistral:7b** along with the available MCP tools
3. Mistral decides to call `read_cv_pdf` → agent forwards this to the MCP server
4. Mistral then calls `score_cv` with the extracted text → agent forwards again
5. Mistral produces a final human-friendly ATS review report
