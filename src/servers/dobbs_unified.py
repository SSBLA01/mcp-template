#!/usr/bin/env python3
"""
Mathematical Research Unified MCP Server
A natural language interface for all mathematical research and file operations
"""

import asyncio
import json
import sys
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path
import uuid

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.utils.common import setup_logging, load_config, ensure_directory

# Import MCP SDK
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Import file operations
from src.servers.file_operations import (
    search_dropbox, list_dropbox_folder, read_dropbox_file, save_to_dropbox,
    copy_file, move_file, delete_file, create_folder,
    FILE_OPERATION_TOOLS
)

# Import GitHub operations
from src.servers.github_operations import (
    list_github_repos, browse_github_repo, read_github_file, create_github_file,
    get_github_repo_info, list_github_commits, search_github,
    GITHUB_OPERATION_TOOLS
)

# Import other server functions
from src.servers.master_coordinator import (
    initiate_research_session, coordinate_workflow, get_session_status, manage_agents,
    INITIATE_SESSION_TOOL, COORDINATE_WORKFLOW_TOOL, GET_SESSION_STATUS_TOOL, MANAGE_AGENTS_TOOL
)
from src.servers.research_discovery import (
    discover_research, analyze_paper, find_related_work, track_research_trends,
    DISCOVER_RESEARCH_TOOL, ANALYZE_PAPER_TOOL, FIND_RELATED_WORK_TOOL, TRACK_RESEARCH_TRENDS_TOOL
)
from src.servers.mathematical_visualization import (
    create_manim_animation, validate_with_wolfram, create_static_diagram, create_interactive_visual,
    CREATE_MANIM_ANIMATION_TOOL, VALIDATE_WITH_WOLFRAM_TOOL, CREATE_STATIC_DIAGRAM_TOOL, CREATE_INTERACTIVE_VISUAL_TOOL
)
from src.servers.knowledge_ingestion import (
    ingest_to_obsidian, sync_to_dropbox, manage_github_repo, create_smart_index,
    INGEST_TO_OBSIDIAN_TOOL, SYNC_TO_DROPBOX_TOOL, MANAGE_GITHUB_REPO_TOOL, CREATE_SMART_INDEX_TOOL
)

# Import Notion operations
from src.servers.notion_operations import (
    search_notion, create_notion_page, update_notion_page, add_to_notion_database,
    list_notion_databases, sync_obsidian_to_notion,
    NOTION_OPERATION_TOOLS
)

# Import Gemini operations
from src.servers.gemini_operations import (
    gemini_query, gemini_analyze_code, gemini_brainstorm, gemini_summarize,
    gemini_math_analysis, gemini_research_review,
    GEMINI_OPERATION_TOOLS
)

# Import Kimi K2 integration with defensive error handling
try:
    from src.servers.kimi_k2_integration import KimiK2Integration
    kimi_available = True
except ImportError as e:
    kimi_available = False
    import logging
    logging.getLogger("MathResearchMCP").warning(f"Kimi K2 integration unavailable: {e}")

# Setup logging
logger = setup_logging("MathResearchMCP")

# Load configuration
config = load_config()

# Initialize MCP server
server = Server("mathematical-research-mcp")

# Initialize Kimi K2 integration if available
kimi_k2 = None
if kimi_available:
    try:
        kimi_k2 = KimiK2Integration(server)
    except Exception as e:
        logger.warning(f"Failed to initialize Kimi K2 integration: {e}")

# Define Kimi K2 tools
KIMI_K2_TOOLS = kimi_k2.tools if kimi_k2 else []

# Combine all tools
ALL_TOOLS = [
    # File operations (most commonly used)
    *FILE_OPERATION_TOOLS,
    
    # GitHub operations
    *GITHUB_OPERATION_TOOLS,
    
    # Research coordination
    INITIATE_SESSION_TOOL,
    COORDINATE_WORKFLOW_TOOL,
    GET_SESSION_STATUS_TOOL,
    MANAGE_AGENTS_TOOL,
    
    # Research discovery
    DISCOVER_RESEARCH_TOOL,
    ANALYZE_PAPER_TOOL,
    FIND_RELATED_WORK_TOOL,
    TRACK_RESEARCH_TRENDS_TOOL,
    
    # Visualization
    CREATE_MANIM_ANIMATION_TOOL,
    VALIDATE_WITH_WOLFRAM_TOOL,
    CREATE_STATIC_DIAGRAM_TOOL,
    CREATE_INTERACTIVE_VISUAL_TOOL,
    
    # Knowledge management
    INGEST_TO_OBSIDIAN_TOOL,
    SYNC_TO_DROPBOX_TOOL,
    MANAGE_GITHUB_REPO_TOOL,
    CREATE_SMART_INDEX_TOOL,
    
    # Notion operations
    *NOTION_OPERATION_TOOLS,
    
    # Gemini operations
    *GEMINI_OPERATION_TOOLS,
    
    # Kimi K2 operations (if available)
    *KIMI_K2_TOOLS
]

# List available tools
@server.list_tools()
async def handle_list_tools() -> List[Tool]:
    """Return all available tools"""
    return ALL_TOOLS

# Tool handler
@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> List[TextContent]:
    """Handle all tool calls"""
    try:
        # File operations
        if name == "search_dropbox":
            result = await search_dropbox(**arguments)
        elif name == "list_dropbox_folder":
            result = await list_dropbox_folder(**arguments)
        elif name == "read_dropbox_file":
            result = await read_dropbox_file(**arguments)
        elif name == "save_to_dropbox":
            result = await save_to_dropbox(**arguments)
        elif name == "copy_file":
            result = await copy_file(**arguments)
        elif name == "move_file":
            result = await move_file(**arguments)
        elif name == "delete_file":
            result = await delete_file(**arguments)
        elif name == "create_folder":
            result = await create_folder(**arguments)
        
        # GitHub operations
        elif name == "list_github_repos":
            result = await list_github_repos(**arguments)
        elif name == "browse_github_repo":
            result = await browse_github_repo(**arguments)
        elif name == "read_github_file":
            result = await read_github_file(**arguments)
        elif name == "create_github_file":
            result = await create_github_file(**arguments)
        elif name == "get_github_repo_info":
            result = await get_github_repo_info(**arguments)
        elif name == "list_github_commits":
            result = await list_github_commits(**arguments)
        elif name == "search_github":
            result = await search_github(**arguments)
        
        # Research coordination
        elif name == "initiate_research_session":
            result = await initiate_research_session(**arguments)
        elif name == "coordinate_workflow":
            result = await coordinate_workflow(**arguments)
        elif name == "get_session_status":
            result = await get_session_status(**arguments)
        elif name == "manage_agents":
            result = await manage_agents(**arguments)
        
        # Research discovery
        elif name == "discover_research":
            result = await discover_research(**arguments)
        elif name == "analyze_paper":
            result = await analyze_paper(**arguments)
        elif name == "find_related_work":
            result = await find_related_work(**arguments)
        elif name == "track_research_trends":
            result = await track_research_trends(**arguments)
        
        # Visualization
        elif name == "create_manim_animation":
            result = await create_manim_animation(**arguments)
        elif name == "validate_with_wolfram":
            result = await validate_with_wolfram(**arguments)
        elif name == "create_static_diagram":
            result = await create_static_diagram(**arguments)
        elif name == "create_interactive_visual":
            result = await create_interactive_visual(**arguments)
        
        # Knowledge management
        elif name == "ingest_to_obsidian":
            result = await ingest_to_obsidian(**arguments)
        elif name == "sync_to_dropbox":
            result = await sync_to_dropbox(**arguments)
        elif name == "manage_github_repo":
            result = await manage_github_repo(**arguments)
        elif name == "create_smart_index":
            result = await create_smart_index(**arguments)
        
        # Notion operations
        elif name == "search_notion":
            result = await search_notion(**arguments)
        elif name == "create_notion_page":
            result = await create_notion_page(**arguments)
        elif name == "update_notion_page":
            result = await update_notion_page(**arguments)
        elif name == "add_to_notion_database":
            result = await add_to_notion_database(**arguments)
        elif name == "list_notion_databases":
            result = await list_notion_databases(**arguments)
        elif name == "sync_obsidian_to_notion":
            result = await sync_obsidian_to_notion(**arguments)
        
        # Gemini operations
        elif name == "gemini_query":
            result = await gemini_query(**arguments)
        elif name == "gemini_analyze_code":
            result = await gemini_analyze_code(**arguments)
        elif name == "gemini_brainstorm":
            result = await gemini_brainstorm(**arguments)
        elif name == "gemini_summarize":
            result = await gemini_summarize(**arguments)
        elif name == "gemini_math_analysis":
            result = await gemini_math_analysis(**arguments)
        elif name == "gemini_research_review":
            result = await gemini_research_review(**arguments)
        
        # Kimi K2 operations
        elif name.startswith("kimi_k2_"):
            if kimi_k2:
                return await kimi_k2.handle_tool_call(name, arguments)
            else:
                result = {
                    "error": "Kimi K2 integration not available. Please install groq: pip install groq",
                    "status": "error"
                }
        
        else:
            result = {"error": f"Unknown tool: {name}"}
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    except Exception as e:
        logger.error(f"Error handling tool {name}: {e}")
        return [TextContent(type="text", text=json.dumps({
            "error": str(e),
            "tool": name,
            "suggestion": "Check the parameters and try again"
        }, indent=2))]

async def main():
    """Main entry point for the MCP server"""
    logger.info("Starting Mathematical Research MCP Server...")
    logger.info(f"Dropbox base path: {config['paths']['dropbox_base']}")
    logger.info(f"Obsidian vault: {config['paths']['obsidian_vault']}")
    logger.info(f"Total tools available: {len(ALL_TOOLS)}")
    
    # Add startup delay to prevent timeout
    logger.info("Initializing server components...")
    await asyncio.sleep(0.5)
    
    # Ensure required directories exist
    ensure_directory(config['paths']['obsidian_vault'])
    ensure_directory(config['paths']['manim_output'])
    
    # Initialize Kimi K2 if available
    if kimi_k2:
        logger.info("Initializing Kimi K2 integration...")
        kimi_k2.register_with_server()
        logger.info("✅ Kimi K2 integration active (4 tools)")
    else:
        logger.warning("⚠️  Kimi K2 integration not available")
    
    # Run the server
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mathematical-research-mcp",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
