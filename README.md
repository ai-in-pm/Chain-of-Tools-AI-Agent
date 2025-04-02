# Chain-of-Tools AI Agent

## Overview

This project implements a real-time Chain-of-Tools AI Agent that demonstrates how a frozen Language Model (LLM) can dynamically decide when to use tools during its generation process. The agent provides a step-by-step visualization of the decision-making process for tool usage.

The development of this repository was inspired by the paper "Chain-of-Tools: Utilizing Massive Unseen Tools in the CoT Reasoning of Frozen Language Models". To read the entire paper, visit https://www.arxiv.org/pdf/2503.16779

https://github.com/user-attachments/assets/ca1ef775-e4b1-48b4-9565-88d4cbbb9185

## Features

- **Real-time Chain-of-Tools**: The agent decides when to use tools during the generation process.
- **Tool Judge Module**: Determines if a tool is needed based on the current hidden state.
- **Tool Retrieval**: Finds the most appropriate tool based on the current context.
- **Interactive Demo**: Allows users to interact with the agent and see the decision-making process.
- **Web Search Integration**: Enables the agent to search the web, find news articles, and fetch content from URLs.

## Directory Structure

```
AI_Agent/
│
├── .env                  # Environment variables and configuration
├── README.md             # This documentation file
├── database/
│   └── agent_data.db     # SQLite database for agent data
├── run_demo.py           # Script to run the demonstration
└── agent/
    ├── __init__.py
    ├── main.py           # Main agent implementation
    ├── llm_loader.py     # LLM loading and token generation
    ├── database.py       # Database management
    ├── tool_database.py  # Tool database management
    ├── interface.py      # User interface for displaying results
    └── tools/
        ├── __init__.py
        ├── tool_judge.py   # Tool Judge module
        ├── query_encoder.py # Query encoder for tool retrieval
        ├── tool_encoder.py  # Tool encoder for tool retrieval
        ├── tool_implementations.py # Basic tool implementations
        └── web_tools.py    # Web search and content fetching tools
```

## Available Tools

### Basic Tools
- **WeatherAPI**: Get weather information for a location and date
- **CapitalAPI**: Find the capital city of a country
- **SearchAPI**: General-purpose search tool
- **CalculatorAPI**: Perform mathematical calculations
- **TranslateAPI**: Translate text between languages

### Web Tools
- **WebSearch**: Search the web for information
- **NewsSearch**: Search for news articles with date filtering
- **WebContentFetcher**: Fetch content from a URL

### Project Management Tools
- **ProjectFileProcessor**: Process and analyze project management files (MPP, XER, etc.)
  - Extract tasks and resources from project files
  - Analyze critical path and project timelines
  - Convert between different project file formats

## Usage

### Running the Demo

```bash
# Run with a sample query
python run_demo.py

# Run with a custom query
python run_demo.py --query "What's the weather in New York today?"

# Run in interactive mode
python run_demo.py --interactive

# Run in debug mode with additional logging
python run_demo.py --debug
```

### Configuration

The agent behavior can be configured through the `.env` file:

```
# Model and Database Paths
MODEL_PATH=models/frozen_llm
DATABASE_PATH=database/agent_data.db

# Tool Configuration
TOOL_JUDGE_THRESHOLD=0.7    # Threshold for tool decision
ENABLE_TOOL_CACHING=True    # Cache tool vectors

# Display Options
DISPLAY_THINKING=True       # Show agent thinking process
DISPLAY_TOKEN_BY_TOKEN=True # Show token generation

# Web Tools Configuration
WEB_SEARCH_MAX_RESULTS=5    # Max results for web search
```

## How It Works

1. **Initialization**: The agent loads the LLM, initializes tools, and sets up the database.
2. **Query Processing**: The user's query is formatted with a Chain of Thought prompt.
3. **Token Generation Loop**:
   - The agent generates tokens one by one.
   - For each token, the Tool Judge determines if a tool is needed.
   - If a tool is needed, the agent finds and calls the appropriate tool.
   - Tool results are integrated into the response.
4. **Response Finalization**: The agent generates a complete response including tool results.

## Implementing New Tools

To add new tools, create a class with static methods in either `tool_implementations.py` or a new file, then update the `tools` dictionary in the `CoToolsAgent` class in `main.py`.

Example:

```python
class MyNewTool:
    @staticmethod
    def perform_action(param1, param2):
        # Tool implementation
        return f"Result: {param1}, {param2}"
```
