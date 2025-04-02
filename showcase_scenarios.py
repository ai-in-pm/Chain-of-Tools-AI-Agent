#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Real-World Scenario Demo for the Chain-of-Tools AI Agent

This script demonstrates the AI Agent's capabilities in solving
real-world tasks using the Chain-of-Tools approach with different
tool combinations.

Author: PhD-Level AI Agent
Date: April 2, 2025
"""

import os
import sys
import time
from dotenv import load_dotenv

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the agent components
from agent.main import CoToolsAgent


def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_scenario_header(scenario_name, description):
    """
    Print a formatted header for a scenario.
    
    Args:
        scenario_name (str): The name of the scenario.
        description (str): A brief description of the scenario.
    """
    print("\n" + "=" * 80)
    print(f"SCENARIO: {scenario_name}")
    print("=" * 80)
    print(f"\n{description}\n")
    print("-" * 80 + "\n")


def run_travel_planning_scenario(agent):
    """
    Run a travel planning scenario demonstration.
    
    Args:
        agent (CoToolsAgent): The initialized agent.
    """
    clear_screen()
    print_scenario_header(
        "Travel Planning", 
        "The user is planning a trip to Paris and needs information about weather, attractions, and local tips."
    )
    
    query = "I'm planning a trip to Paris next week. What's the weather forecast, what are the must-see attractions, and any local tips I should know?"
    
    print(f"User Query: {query}\n")
    time.sleep(1)
    
    # Process the query using the agent
    answer = agent.process_query(query)
    
    print("\nScenario complete!\n")
    input("Press Enter to continue to the next scenario...")


def run_research_scenario(agent):
    """
    Run a research scenario demonstration.
    
    Args:
        agent (CoToolsAgent): The initialized agent.
    """
    clear_screen()
    print_scenario_header(
        "Academic Research", 
        "The user is researching renewable energy and needs to find recent articles and data."
    )
    
    query = "I'm doing research on solar energy advancements. Can you find recent academic articles and summarize the key findings about efficiency improvements?"
    
    print(f"User Query: {query}\n")
    time.sleep(1)
    
    # Process the query using the agent
    answer = agent.process_query(query)
    
    print("\nScenario complete!\n")
    input("Press Enter to continue to the next scenario...")


def run_calculation_scenario(agent):
    """
    Run a calculation scenario demonstration.
    
    Args:
        agent (CoToolsAgent): The initialized agent.
    """
    clear_screen()
    print_scenario_header(
        "Complex Calculation", 
        "The user needs to perform a complex calculation and interpret the results."
    )
    
    query = "If I invest $10,000 with an annual interest rate of 5.75% compounded monthly, how much will I have after 10 years? And how much of that will be interest?"
    
    print(f"User Query: {query}\n")
    time.sleep(1)
    
    # Process the query using the agent
    answer = agent.process_query(query)
    
    print("\nScenario complete!\n")
    input("Press Enter to continue to the next scenario...")


def run_translation_scenario(agent):
    """
    Run a translation scenario demonstration.
    
    Args:
        agent (CoToolsAgent): The initialized agent.
    """
    clear_screen()
    print_scenario_header(
        "Language Translation", 
        "The user needs to translate text and understand cultural context."
    )
    
    query = "I received an email in French that says 'Je suis ravi de vous rencontrer la semaine prochaine.' What does it mean and how should I respond politely?"
    
    print(f"User Query: {query}\n")
    time.sleep(1)
    
    # Process the query using the agent
    answer = agent.process_query(query)
    
    print("\nScenario complete!\n")
    input("Press Enter to continue to the next scenario...")


def run_news_analysis_scenario(agent):
    """
    Run a news analysis scenario demonstration.
    
    Args:
        agent (CoToolsAgent): The initialized agent.
    """
    clear_screen()
    print_scenario_header(
        "News Analysis", 
        "The user wants to understand recent events and their implications."
    )
    
    query = "What are the major global economic news from the past week, and how might they affect international markets?"
    
    print(f"User Query: {query}\n")
    time.sleep(1)
    
    # Process the query using the agent
    answer = agent.process_query(query)
    
    print("\nScenario complete!\n")
    input("Press Enter to continue to the next scenario...")


def run_project_management_scenario(agent):
    """
    Run a project management scenario demonstration.
    
    Args:
        agent (CoToolsAgent): The initialized agent.
    """
    clear_screen()
    print_scenario_header(
        "Project Management", 
        "The user needs to analyze a project schedule file and get recommendations."
    )
    
    query = "I have a project file called 'new_product_launch.mpp'. Can you extract the key tasks, analyze the critical path, and recommend any optimization opportunities?"
    
    print(f"User Query: {query}\n")
    time.sleep(1)
    
    # Process the query using the agent
    answer = agent.process_query(query)
    
    print("\nScenario complete!\n")
    input("Press Enter to finish the demonstration...")


def main():
    """
    Main function to run the real-world scenario demonstration.
    """
    # Load environment variables
    load_dotenv()
    
    # Set environment variables for demonstration
    os.environ["DISPLAY_THINKING"] = "True"
    os.environ["DISPLAY_TOKEN_BY_TOKEN"] = "False"  # Changed to False for cleaner demo
    
    # Initialize the agent
    print("Initializing the Chain-of-Tools AI Agent...")
    agent = CoToolsAgent()
    if not agent.initialize():
        print("Failed to initialize the agent. Exiting.")
        return
    
    # Create necessary directories if they don't exist
    os.makedirs("database", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    
    # Welcome message
    clear_screen()
    print("\n" + "*" * 80)
    print("*" + " " * 78 + "*")
    print("*" + " " * 23 + "CHAIN-OF-TOOLS AI AGENT SHOWCASE" + " " * 23 + "*")
    print("*" + " " * 78 + "*")
    print("*" * 80 + "\n")
    
    print("Welcome to the Chain-of-Tools AI Agent Real-World Scenario Demo!\n")
    print("This demonstration will showcase the agent's ability to use different")
    print("tools in real-time to solve complex tasks across various domains.\n")
    print("NOTE: This is a simulated demonstration. The tools don't actually connect")
    print("to real APIs or services.\n")
    input("Press Enter to begin the demonstration...")
    
    # Run the scenarios
    run_travel_planning_scenario(agent)
    run_research_scenario(agent)
    run_calculation_scenario(agent)
    run_translation_scenario(agent)
    run_news_analysis_scenario(agent)
    run_project_management_scenario(agent)
    
    # Farewell message
    clear_screen()
    print("\n" + "*" * 80)
    print("\nThank you for exploring the Chain-of-Tools AI Agent!\n")
    print("This demonstration showcased how the agent dynamically selects and")
    print("uses different tools to solve complex real-world tasks.\n")
    print("For more information, please refer to the README.md file.\n")
    print("*" * 80 + "\n")


if __name__ == "__main__":
    main()
