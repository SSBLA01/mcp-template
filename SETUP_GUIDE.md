# MCP Mathematical Research Setup Guide

This guide will walk you through setting up your Mathematical Research MCP template from scratch.

## 📋 Prerequisites Checklist

Before starting, make sure you have:

- [ ] **Python 3.8 or higher** installed
- [ ] **Claude Desktop** application installed
- [ ] **Git** installed for version control
- [ ] **Basic familiarity** with command line/terminal
- [ ] **Text editor** (VS Code, nano, etc.)

## 🔑 Step 1: API Keys Setup

You'll need to obtain API keys from several services. Here's how:

### 1.1 Perplexity AI
1. Go to [perplexity.ai](https://perplexity.ai)
2. Sign up/login
3. Navigate to Settings → API
4. Generate a new API key
5. Copy and save securely

### 1.2 Wolfram Alpha
1. Visit [developer.wolframalpha.com](https://developer.wolframalpha.com)
2. Create a developer account
3. Create a new app
4. Copy the App ID (not the full key)

### 1.3 Dropbox
1. Go to [dropbox.com/developers](https://dropbox.com/developers)
2. Click "Create apps"
3. Choose "Scoped access" and "Full Dropbox"
4. Name your app (e.g., "MathResearch-MCP")
5. Copy App key and App secret
6. Under "Permissions" tab, enable:
   - `files.content.write`
   - `files.content.read` 
   - `files.metadata.read`
   - `files.metadata.write`

### 1.4 GitHub
1. Go to GitHub → Settings → Developer settings
2. Click "Personal access tokens" → "Tokens (classic)"
3. Generate new token with these scopes:
   - `repo` (full control of private repositories)
   - `user` (read user profile data)
4. Copy the token immediately (won't be shown again)

### 1.5 Notion
1. Go to [notion.so/my-integrations](https://notion.so/my-integrations)
2. Click "New integration"
3. Name it "Math Research MCP"
4. Select your workspace
5. Copy the Internal Integration Token

### 1.6 Google Gemini
1. Visit [makersuite.google.com](https://makersuite.google.com)
2. Sign in with Google account
3. Click "Get API key"
4. Create a new API key
5. Copy and save securely

## 📁 Step 2: Directory Structure Setup

Create the following directory structure on your system:

```bash
# Create main directories (adjust paths for your system)
mkdir -p ~/MathResearch
mkdir -p ~/MathResearch/Obsidian_Vault
mkdir -p ~/MathResearch/Manim_Outputs
mkdir -p ~/MathResearch/System_Files
mkdir -p ~/MathResearch/Inbox
mkdir -p ~/MathResearch/Knowledge
```

**Note the full paths** - you'll need these for configuration:
- Obsidian Vault: `/Users/YOUR_USERNAME/MathResearch/Obsidian_Vault`
- Manim Outputs: `/Users/YOUR_USERNAME/MathResearch/Manim_Outputs`
- System Base: `/Users/YOUR_USERNAME/MathResearch`

## ⚙️ Step 3: Environment Configuration

### 3.1 Create Environment File
```bash
# In your project directory
cp .env.example .env
```

### 3.2 Edit .env File
Open `.env` in your text editor and fill in:

```bash
# API Keys - Replace with your actual keys
PERPLEXITY_API_KEY=your_actual_perplexity_key_here
WOLFRAM_ALPHA_APP_ID=your_actual_wolfram_app_id_here
DROPBOX_APP_KEY=your_actual_dropbox_app_key_here
DROPBOX_APP_SECRET=your_actual_dropbox_app_secret_here
DROPBOX_ACCESS_TOKEN=  # Leave empty for now
GITHUB_TOKEN=your_actual_github_token_here
NOTION_TOKEN=your_actual_notion_token_here
GEMINI_API_KEY=your_actual_gemini_key_here

# Paths - Update with YOUR actual paths
OBSIDIAN_VAULT_PATH=/Users/YOUR_USERNAME/MathResearch/Obsidian_Vault
MANIM_OUTPUT_DIR=/Users/YOUR_USERNAME/MathResearch/Manim_Outputs
DROPBOX_BASE_PATH=/Users/YOUR_USERNAME/MathResearch

# Dashboard Configuration
NEXT_PUBLIC_MCP_WS_URL=ws://localhost:8080
NEXT_PUBLIC_OBSIDIAN_API_PORT=27124
NEXT_PUBLIC_OBSIDIAN_VAULT_PATH=/Users/YOUR_USERNAME/MathResearch/Obsidian_Vault

# Settings
MANIM_QUALITY=medium_quality
LOG_LEVEL=INFO
```

**Important**: Replace `YOUR_USERNAME` with your actual username!

## 🐍 Step 4: Python Environment Setup

### 4.1 Create Virtual Environment
```bash
# In your project directory
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\\Scripts\\activate
```

### 4.2 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4.3 Verify Installation
```bash
python -c "import mcp; print('MCP SDK installed successfully')"
```

## 🖥️ Step 5: Claude Desktop Configuration

### 5.1 Find Config File Location
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\\Claude\\claude_desktop_config.json`

### 5.2 Update Configuration
Replace `FULL_PATH_TO_YOUR_REPO` with your actual repository path:

```json
{
  "mcpServers": {
    "Mathematical-Research-MCP": {
      "command": "bash",
      "args": ["/FULL/PATH/TO/YOUR/REPO/run_dobbs_mcp.sh"],
      "cwd": "/FULL/PATH/TO/YOUR/REPO",
      "env": {
        "PYTHONPATH": "/FULL/PATH/TO/YOUR/REPO"
      }
    }
  }
}
```

**Example** (macOS):
```json
{
  "mcpServers": {
    "Mathematical-Research-MCP": {
      "command": "bash",
      "args": ["/Users/johndoe/MathResearch/mcp-template/run_dobbs_mcp.sh"],
      "cwd": "/Users/johndoe/MathResearch/mcp-template",
      "env": {
        "PYTHONPATH": "/Users/johndoe/MathResearch/mcp-template"
      }
    }
  }
}
```

### 5.3 Make Script Executable
```bash
chmod +x run_dobbs_mcp.sh
```

## 🎯 Step 6: Obsidian Setup

### 6.1 Install Obsidian
Download from [obsidian.md](https://obsidian.md)

### 6.2 Create Vault
1. Open Obsidian
2. Choose "Create new vault"
3. Select your Obsidian directory: `/Users/YOUR_USERNAME/MathResearch/Obsidian_Vault`
4. Name it "Mathematical Research"

### 6.3 Recommended Plugins
Install these community plugins:
- **Zettelkasten Prefixer** - For unique note IDs
- **Graph Analysis** - Visualize connections
- **Dataview** - Query your notes
- **Citations** - Manage references

## 🧪 Step 7: Testing Your Setup

### 7.1 Test Server Independently
```bash
# In your project directory with venv activated
python src/servers/dobbs_unified.py
```

You should see initialization messages. Press Ctrl+C to stop.

### 7.2 Test Claude Desktop Integration
1. **Restart Claude Desktop** completely
2. Open a new conversation
3. Type: "List my available MCP tools"
4. You should see a list of 130+ tools

### 7.3 Basic Functionality Test
Try these commands in Claude:

```
"Create a test folder in my file system called 'mcp-test'"
```

```
"Create a simple note in my Obsidian vault about MCP setup"
```

```
"Search for any mathematical papers about topology"
```

## 🚨 Troubleshooting

### Common Issues

**"Server won't start"**
- Check all API keys are correct in `.env`
- Verify Python virtual environment is activated
- Ensure all dependencies installed: `pip install -r requirements.txt`

**"Claude doesn't see the server"**
- Verify absolute paths in Claude Desktop config
- Check script permissions: `ls -la run_dobbs_mcp.sh`
- Restart Claude Desktop after config changes

**"API errors"**
- Verify API key formats (no extra spaces)
- Check API key permissions and quotas
- Test individual APIs with simple requests

**"Path errors"**
- Ensure all directories exist: `ls -la ~/MathResearch/`
- Check path formatting (no trailing slashes)
- Verify user permissions on directories

### Debug Commands
```bash
# Check environment variables
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Obsidian:', os.environ.get('OBSIDIAN_VAULT_PATH'))"

# Test specific module
python -c "from src.utils.common import load_config; print(load_config())"

# Verify Claude config
cat "$HOME/Library/Application Support/Claude/claude_desktop_config.json"  # macOS
```

## ✅ Step 8: Success Validation

Your setup is complete when:

- [ ] **Server starts** without errors
- [ ] **Claude Desktop** shows 130+ available tools
- [ ] **File operations** work (create/read files)
- [ ] **Obsidian integration** functions
- [ ] **API calls** succeed (search papers, etc.)
- [ ] **Manim animations** can be created

## 🎉 Next Steps

Once setup is complete:

1. **Explore the tools** - Try different MCP functions
2. **Create your first research workflow** - Search papers, create notes, generate visualizations
3. **Customize for your domain** - Adapt folder structures and workflows
4. **Build your knowledge base** - Start using Obsidian for research notes

## 📞 Support

If you encounter issues:

1. **Check the troubleshooting section** above
2. **Review error messages** carefully
3. **Test components individually** (Python, APIs, etc.)
4. **Create detailed issue reports** with error logs

Remember: This is a powerful research tool - take time to learn its capabilities!
