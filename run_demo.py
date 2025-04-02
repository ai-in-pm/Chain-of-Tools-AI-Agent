#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chain-of-Tools AI Agent Demonstration

This script provides a command-line interface to run the Chain-of-Tools AI Agent
and demonstrate its real-time capabilities with different queries.

Author: PhD-Level AI Agent
Date: April 2, 2025
"""

import os
import sys
import argparse

# Handle dotenv import error
try:
    from dotenv import load_dotenv
except ImportError:
    print("Warning: python-dotenv not found. Environment variables will not be loaded from .env file.")
    # Define a dummy load_dotenv function that does nothing
    def load_dotenv():
        print("(Using dummy load_dotenv function)")
        pass

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the CoToolsAgent class
from agent.main import CoToolsAgent


def parse_args():
    """
    Parse command line arguments for the demonstration script.
    
    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Run the Chain-of-Tools AI Agent demonstration")
    parser.add_argument(
        "-q", "--query", type=str,
        help="User query to process. If not provided, a sample query will be used."
    )
    parser.add_argument(
        "-i", "--interactive", action="store_true",
        help="Run in interactive mode, allowing the user to input multiple queries."
    )
    parser.add_argument(
        "-a", "--auto-demo", action="store_true",
        help="Run a predetermined set of demonstrations automatically."
    )
    parser.add_argument(
        "-d", "--debug", action="store_true",
        help="Run in debug mode with additional logging."
    )
    return parser.parse_args()


def run_demo(query=None, debug=False):
    """
    Run the Chain-of-Tools AI Agent demonstration with a specific query.
    
    Args:
        query (str, optional): User query to process. If None, a sample query will be used.
        debug (bool, optional): Whether to run in debug mode. Defaults to False.
    
    Returns:
        str: The final answer from the agent.
    """
    # Load environment variables
    load_dotenv()
    
    # If debug mode is enabled, set environment variable
    if debug:
        os.environ["DISPLAY_THINKING"] = "True"
        os.environ["DISPLAY_TOKEN_BY_TOKEN"] = "True"
    else:
        os.environ["DISPLAY_THINKING"] = "True"
        os.environ["DISPLAY_TOKEN_BY_TOKEN"] = "False"
    
    # Create necessary directories
    os.makedirs("database", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    
    # Initialize the agent
    print("\n" + "=" * 80)
    print("Chain-of-Tools AI Agent Demonstration")
    print("=" * 80)
    
    agent = CoToolsAgent()
    if not agent.initialize():
        print("❌ Failed to initialize the agent.")
        return None
    
    # Use the provided query or a sample query
    if query is None:
        query = "What was the weather in Paris yesterday, and what's the capital of France?"
    
    print("\n📝 Query:")
    print(f"   {query}\n")
    
    # Process the query
    print("⚙️ Processing...\n")
    answer = agent.process_query(query)
    
    # Display the answer
    print("\n✅ Answer:")
    print(f"   {answer}\n")
    
    return answer


def interactive_mode(debug=False):
    """
    Run the Chain-of-Tools AI Agent in interactive mode, allowing the user to input multiple queries.
    
    Args:
        debug (bool, optional): Whether to run in debug mode. Defaults to False.
    """
    # Initialize the agent
    print("\n" + "=" * 80)
    print("Chain-of-Tools AI Agent Interactive Demo")
    print("=" * 80)
    print("\nType 'exit', 'quit', or press Ctrl+C to exit.\n")
    
    # Load environment variables
    load_dotenv()
    
    # If debug mode is enabled, set environment variable
    if debug:
        os.environ["DISPLAY_THINKING"] = "True"
        os.environ["DISPLAY_TOKEN_BY_TOKEN"] = "True"
    
    # Initialize the agent
    agent = CoToolsAgent()
    if not agent.initialize():
        print("❌ Failed to initialize the agent.")
        return
    
    try:
        while True:
            # Get user query
            query = input("\n🔍 Enter your query: ")
            
            # Check if the user wants to exit
            if query.lower() in ["exit", "quit"]:
                print("\n👋 Exiting the demonstration. Goodbye!")
                break
            
            # Process the query
            print("\n⚙️ Processing...\n")
            answer = agent.process_query(query)
            
            # Display the answer
            print("\n✅ Answer:")
            print(f"   {answer}\n")
            
            print("-" * 80)
    except KeyboardInterrupt:
        print("\n\n👋 Exiting the demonstration. Goodbye!")


def auto_demo_mode(debug=False):
    """
    Run a predetermined set of demonstrations without requiring user input.
    
    Args:
        debug (bool, optional): Whether to run in debug mode. Defaults to False.
    """
    # Initialize the agent
    print("\n" + "=" * 80)
    print("Chain-of-Tools AI Agent Auto Demo")
    print("=" * 80)
    print("\nRunning through demonstration scenarios automatically...\n")
    
    # Load environment variables
    load_dotenv()
    
    # Configure display options
    os.environ["DISPLAY_THINKING"] = "True"
    os.environ["DISPLAY_TOKEN_BY_TOKEN"] = "False"  # Always off for auto demo for readability
    
    # Create necessary directories
    os.makedirs("database", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    
    # Initialize the agent
    agent = CoToolsAgent()
    if not agent.initialize():
        print("Failed to initialize the agent.")
        return
    
    # Predefined demonstration queries
    demos = [
        {"name": "Weather Information", "query": "What's the weather like in New York today?"},
        {"name": "Capital Lookup", "query": "What is the capital of France?"},
        {"name": "Math Calculation", "query": "Calculate 125 * 37 / 5"},
        {"name": "Language Translation", "query": "Translate 'hello' to French"},
        {"name": "Project Management", "query": "I have a project file called 'new_product_launch.mpp'. Can you extract the key tasks?"}
    ]
    
    # Run each demonstration
    for i, demo in enumerate(demos, 1):
        print("\n" + "-" * 80)
        print(f"Demonstration {i}: {demo['name']}")
        print("-" * 80)
        
        print(f"\nQuery: {demo['query']}\n")
        
        # Process the query
        print("Processing...\n")
        answer = agent.process_query(demo['query'])
        
        # Display the answer
        print("\nAnswer:")
        print(f"   {answer}\n")
        
        # Pause between demos for readability
        if i < len(demos):
            print("\nPreparing next demonstration...")
            print("-" * 80)
    
    print("\nAuto demonstration complete!")
    print("The Chain-of-Tools AI Agent successfully demonstrated various tool capabilities.")


def main():
    """
    Main function to run the demonstration script.
    """
    # Parse command line arguments
    args = parse_args()
    
    # Additional auto-demo option
    if hasattr(args, 'auto_demo') and args.auto_demo:
        auto_demo_mode(args.debug)
    # Run in interactive mode if specified
    elif args.interactive:
        interactive_mode(args.debug)
    else:
        # Run with the provided query or a sample query
        run_demo(args.query, args.debug)


if __name__ == "__main__":
    main()
