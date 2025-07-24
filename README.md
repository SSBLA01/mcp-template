# MCP Mathematical Research Template

**A comprehensive Model Context Protocol (MCP) server for mathematical research, knowledge management, and intelligent automation.**

## 🚀 Overview

This template provides a unified MCP server with 130+ integrated tools for mathematical research management, knowledge organization, and intelligent automation. Perfect for researchers, mathematicians, and anyone working with complex mathematical concepts.

### Key Features
- **130+ Integrated Tools**: File operations, research discovery, visualization, knowledge management
- **Multi-Platform Integration**: Dropbox, GitHub, Obsidian, Notion, Gemini AI, Perplexity, Wolfram Alpha
- **Mathematical Visualization**: Manim animations with advanced mathematical support
- **Intelligent Automation**: Smart file organization and research workflows
- **Privacy-First Architecture**: Clear separation between private research and public content
- **Knowledge Management**: Zettelkasten methodology with Obsidian integration

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8+**
- **Claude Desktop** installed
- **API Keys** for the following services:
  - Perplexity AI
  - Wolfram Alpha
  - Dropbox
  - GitHub Personal Access Token
  - Notion Integration Token
  - Google Gemini API
- **Optional**: Docker Desktop, Mathematica

## 🎯 Quick Start

### 1. Create Your Repository

Click the **"Use this template"** button at the top of this repository to create your own copy.

### 2. Clone and Setup

```bash
# Clone your new repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your API keys and paths
nano .env  # or your preferred editor
```

Update the following in your `.env` file:
- Replace all `your_*_api_key_here` with actual API keys
- Update all `/path/to/your/` entries with your actual system paths
- Set your preferred output directories

### 4. Claude Desktop Configuration

Add to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\\Claude\\claude_desktop_config.json`

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

**Important**: Use full absolute paths in the configuration.

### 5. Test Your Setup

```bash
# Make the run script executable
chmod +x run_dobbs_mcp.sh

# Test the server
python src/servers/dobbs_unified.py
```

Restart Claude Desktop after configuration.

## 🔑 API Keys Setup

### Required API Keys

1. **Perplexity AI**: Sign up at [perplexity.ai](https://perplexity.ai) → Settings → API
2. **Wolfram Alpha**: Get App ID at [developer.wolframalpha.com](https://developer.wolframalpha.com)
3. **Dropbox**: Create app at [dropbox.com/developers](https://dropbox.com/developers)
4. **GitHub**: Generate token at GitHub → Settings → Developer settings → Personal access tokens
5. **Notion**: Create integration at [notion.so/my-integrations](https://notion.so/my-integrations)
6. **Google Gemini**: Get API key at [makersuite.google.com](https://makersuite.google.com)

### API Key Security
- Never commit actual API keys to version control
- Use environment variables for all sensitive information
- Regularly rotate your API keys
- Monitor API usage and set up billing alerts

## 🛠️ Tool Categories

### File Operations (8 tools)
- Search, read, write, and manage files in Dropbox
- Full CRUD operations with binary file support
- Smart path handling and organization

### GitHub Operations (7 tools)
- Repository management and file operations
- Search across code and repositories
- Commit tracking and metadata retrieval

### Research Discovery (4 tools)
- Academic paper search via Perplexity and arXiv
- Related work analysis and discovery
- Research trend tracking

### Mathematical Visualization (4 tools)
- Manim animation generation
- Wolfram Alpha integration for validation
- Static and interactive diagram creation

### Knowledge Management (4 tools)
- Obsidian vault integration with Zettelkasten methodology
- Smart categorization and indexing
- Cross-platform synchronization

### AI Integration (6 tools)
- Gemini AI for analysis, brainstorming, and research review
- Code analysis and security assessment
- Mathematical concept exploration

## 🔒 Privacy & Security

### Privacy Architecture
- **Obsidian = PRIVATE**: All research stays in your local system
- **Notion = PUBLIC**: Use only for content you want to share
- **NO AUTO-SYNC**: Manual control over all publishing
- **Local Storage**: Sensitive data never leaves your system

### Security Features
- Environment variable encryption for API keys
- Path validation prevents unauthorized access
- Comprehensive error logging
- Sandboxed file operations

## ⚙️ Configuration

### Directory Structure
Create these directories in your system:
```
/your/dropbox/path/
├── 00_MCP_Obsidian_Vault/     # Your Zettelkasten
├── 00_MCP_SYSTEM/             # System files and logs
├── 00_MCP_INBOX/              # Processing inbox
├── MathematicalResearch/      # Research outputs
│   └── manim_outputs/         # Animation outputs
└── Knowledge/                 # General knowledge storage
```

### Obsidian Setup
1. Install Obsidian
2. Create a vault in your designated Obsidian path
3. Install recommended plugins:
   - Zettelkasten Prefixer
   - Graph Analysis
   - Citations
   - Dataview

## 🎨 Creating Mathematical Animations

```python
# Example usage in Claude
"Create a Manim animation showing the gyroaddition formula in hyperbolic geometry"

# The system will:
# 1. Generate appropriate Manim code
# 2. Render the animation
# 3. Save to your specified output directory
# 4. Create accompanying documentation
```

## 🧪 Testing Your Setup

### Basic Functionality Test
Ask Claude (after restart):
```
"Search my Dropbox for any files containing 'test' and create a simple note in my Obsidian vault"
```

### Research Workflow Test
```
"Find recent papers on hyperbolic geometry, create a summary note, and generate a visualization of the main concepts"
```

### Mathematical Validation Test
```
"Validate this equation using Wolfram Alpha: x^2 + y^2 = r^2, then create a Manim animation showing the unit circle"
```

## 🐛 Troubleshooting

### Common Issues

**Server won't start**
- Verify all API keys are correctly set in `.env`
- Check Python version (must be 3.8+)
- Ensure virtual environment is activated
- Review paths in Claude Desktop config

**Claude Desktop doesn't see the server**
- Use absolute paths in configuration
- Restart Claude Desktop after making changes
- Check file permissions on `run_dobbs_mcp.sh`
- Verify the script is executable (`chmod +x`)

**API Errors**
- Validate API key formats and permissions
- Check rate limits for each service
- Verify network connectivity
- Monitor API usage quotas

**File Operation Failures**
- Ensure Dropbox paths exist and are accessible
- Check file permissions
- Verify adequate disk space
- Confirm Dropbox sync status

### Debug Commands
```bash
# Test environment variables
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Dropbox path:', os.environ.get('DROPBOX_BASE_PATH'))"

# Test specific functionality
python src/servers/dobbs_unified.py --test

# Check logs
tail -f logs/mcp.log  # if logs directory exists
```

## 📚 Documentation

### Key Files
- `CLAUDE.md` - Detailed Claude integration guide
- `CONFIGURATION_STATUS.md` - Setup verification checklist
- `examples/` - Usage examples and templates
- `docs/` - Comprehensive documentation

### Learning Resources
- [MCP Documentation](https://modelcontextprotocol.io)
- [Obsidian Documentation](https://obsidian.md)
- [Manim Documentation](https://manim.community)

## 🔄 Updates and Maintenance

### Keeping Your Template Updated
1. Check the original template repository for updates
2. Review changelog for new features
3. Update your API integrations as needed
4. Test functionality after updates

### Contributing Back
If you create useful extensions or improvements:
1. Fork the original template repository
2. Create a feature branch
3. Submit a pull request
4. Help improve the template for everyone

## 📞 Support

- **Documentation Issues**: Create an issue in your repository
- **Setup Questions**: Check the troubleshooting section first
- **Feature Requests**: Consider contributing or suggesting improvements

## 📄 License

MIT License - See LICENSE file for details

---

**Happy researching! 🔬✨**

*This template provides the foundation for powerful mathematical research workflows. Customize it to fit your specific needs and research domains.*
