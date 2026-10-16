# server.py -- MCP Server
# This file NEVER changes when you add a new tool.
# Steps to add a tool:
#   1. Create tools/<your_tool>.py  with a plain Python function
#   2. Import it here and call mcp.tool()(your_function)
#   That is all. The agent.py stays exactly the same.

from mcp.server.fastmcp import FastMCP

# Import tool functions (one file per tool)
from tools.read_cv_pdf import read_cv_pdf   # <-- Tool 1
from tools.score_cv    import score_cv       # <-- Tool 2
# from tools.your_tool import your_tool     # <-- Add Tool 3 here

# Create the server and register tools
mcp = FastMCP("ATS CV Reviewer")
mcp.tool()(read_cv_pdf)   # register Tool 1
#mcp.tool()(score_cv)      # register Tool 2

if __name__ == "__main__":
    mcp.run(transport="stdio")