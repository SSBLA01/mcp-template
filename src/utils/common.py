"""
Common utilities for Mathematical Research MCP
Provides configuration loading, logging setup, and directory management
"""

import os
import logging
import json
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

def setup_logging(name: str = "MathResearchMCP", level: str = "INFO") -> logging.Logger:
    """
    Set up logging for the application
    
    Args:
        name: Logger name
        level: Logging level
        
    Returns:
        Configured logger instance
    """
    # Load environment variables
    load_dotenv()
    
    # Get log level from environment or use default
    log_level = os.getenv("LOG_LEVEL", level)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Avoid duplicate handlers
    if not logger.handlers:
        # Create console handler
        handler = logging.StreamHandler()
        handler.setLevel(getattr(logging, log_level.upper()))
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(handler)
    
    return logger

def load_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables
    
    Returns:
        Configuration dictionary with all required settings
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get base paths with defaults
    dropbox_base = os.getenv("DROPBOX_BASE_PATH", os.path.expanduser("~/Dropbox"))
    obsidian_vault = os.getenv("OBSIDIAN_VAULT_PATH", os.path.join(dropbox_base, "Obsidian_Vault"))
    manim_output = os.getenv("MANIM_OUTPUT_DIR", os.path.join(dropbox_base, "Manim_Outputs"))
    
    config = {
        # API Keys
        "api_keys": {
            "perplexity": os.getenv("PERPLEXITY_API_KEY"),
            "wolfram": os.getenv("WOLFRAM_ALPHA_APP_ID"),
            "dropbox_app_key": os.getenv("DROPBOX_APP_KEY"),
            "dropbox_app_secret": os.getenv("DROPBOX_APP_SECRET"),
            "dropbox_access_token": os.getenv("DROPBOX_ACCESS_TOKEN"),
            "github": os.getenv("GITHUB_TOKEN"),
            "notion": os.getenv("NOTION_TOKEN"),
            "gemini": os.getenv("GEMINI_API_KEY"),
            "groq": os.getenv("GROQ_API_KEY")  # For Kimi K2
        },
        
        # File paths
        "paths": {
            "dropbox_base": dropbox_base,
            "obsidian_vault": obsidian_vault,
            "manim_output": manim_output,
            "system_files": os.path.join(dropbox_base, "System_Files"),
            "inbox": os.path.join(dropbox_base, "Inbox"),
            "knowledge": os.path.join(dropbox_base, "Knowledge")
        },
        
        # Dashboard configuration
        "dashboard": {
            "ws_url": os.getenv("NEXT_PUBLIC_MCP_WS_URL", "ws://localhost:8080"),
            "obsidian_api_port": int(os.getenv("NEXT_PUBLIC_OBSIDIAN_API_PORT", "27124")),
            "obsidian_vault_path": obsidian_vault
        },
        
        # Settings
        "settings": {
            "manim_quality": os.getenv("MANIM_QUALITY", "medium_quality"),
            "log_level": os.getenv("LOG_LEVEL", "INFO"),
            "max_file_size": int(os.getenv("MAX_FILE_SIZE", "10485760")),  # 10MB default
            "request_timeout": int(os.getenv("REQUEST_TIMEOUT", "30"))  # 30 seconds
        }
    }
    
    return config

def ensure_directory(path: str) -> bool:
    """
    Ensure a directory exists, create it if it doesn't
    
    Args:
        path: Directory path to ensure exists
        
    Returns:
        True if directory exists or was created successfully
    """
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        logger = logging.getLogger("MathResearchMCP")
        logger.error(f"Failed to create directory {path}: {e}")
        return False

def validate_api_keys(config: Dict[str, Any]) -> Dict[str, bool]:
    """
    Validate that required API keys are present
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Dictionary with validation status for each API key
    """
    required_keys = [
        "perplexity", "wolfram", "dropbox_app_key", 
        "dropbox_app_secret", "github", "notion", "gemini"
    ]
    
    validation = {}
    api_keys = config.get("api_keys", {})
    
    for key in required_keys:
        value = api_keys.get(key)
        validation[key] = bool(value and value.strip() and not value.startswith("your_"))
    
    return validation

def get_safe_filename(filename: str) -> str:
    """
    Convert a string to a safe filename by removing/replacing invalid characters
    
    Args:
        filename: Original filename
        
    Returns:
        Safe filename string
    """
    import re
    
    # Replace invalid characters with underscores
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    # Remove multiple consecutive underscores
    safe_name = re.sub(r'_+', '_', safe_name)
    
    # Remove leading/trailing underscores and spaces
    safe_name = safe_name.strip('_ ')
    
    # Ensure it's not empty
    if not safe_name:
        safe_name = "untitled"
    
    return safe_name

def format_error_response(error: Exception, context: str = "") -> Dict[str, Any]:
    """
    Format an error into a standard response structure
    
    Args:
        error: Exception that occurred
        context: Additional context about where the error occurred
        
    Returns:
        Formatted error response dictionary
    """
    return {
        "status": "error",
        "error": str(error),
        "context": context,
        "type": type(error).__name__
    }

def format_success_response(data: Any, message: str = "") -> Dict[str, Any]:
    """
    Format a success response into a standard structure
    
    Args:
        data: Response data
        message: Optional success message
        
    Returns:
        Formatted success response dictionary
    """
    response = {
        "status": "success",
        "data": data
    }
    
    if message:
        response["message"] = message
    
    return response

def check_environment_setup() -> Dict[str, Any]:
    """
    Check if the environment is properly set up
    
    Returns:
        Dictionary with setup status information
    """
    config = load_config()
    
    # Check API keys
    api_validation = validate_api_keys(config)
    
    # Check directories
    directories = config["paths"]
    directory_status = {}
    
    for name, path in directories.items():
        directory_status[name] = {
            "path": path,
            "exists": os.path.exists(path),
            "writable": os.access(path, os.W_OK) if os.path.exists(path) else False
        }
    
    return {
        "api_keys": api_validation,
        "directories": directory_status,
        "config_loaded": True,
        "environment_file_exists": os.path.exists(".env")
    }

# Create a default logger for this module
logger = setup_logging(__name__)

# Log configuration loading
try:
    config = load_config()
    logger.info("Configuration loaded successfully")
except Exception as e:
    logger.error(f"Failed to load configuration: {e}")
