# Database Module for AI Agent

import sqlite3
import os
import json

class AgentDatabase:
    """
    Class for managing the embedded SQLite database for the AI Agent.
    """
    
    def __init__(self, db_path):
        """
        Initialize the database with the given path.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """
        Connect to the SQLite database.
        
        Returns:
            bool: True if connection successful, False otherwise.
        """
        try:
            # Ensure the directory exists
            db_dir = os.path.dirname(self.db_path)
            if not os.path.exists(db_dir):
                os.makedirs(db_dir)
                print(f"Created database directory: {db_dir}")
                
            # Connect to the database (will create it if it doesn't exist)
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            print(f"Connected to database: {self.db_path}")
            return True
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return False
    
    def disconnect(self):
        """
        Disconnect from the SQLite database.
        """
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
    
    def initialize_database(self):
        """
        Initialize the database by creating necessary tables if they don't exist.
        
        Returns:
            bool: True if initialization successful, False otherwise.
        """
        if not self.conn:
            if not self.connect():
                return False
        
        try:
            # Create tools table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tools (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    vector_data TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create logs table for storing interaction logs
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    user_query TEXT,
                    agent_response TEXT,
                    tools_used TEXT
                )
            """)
            
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            return False
    
    def add_tool(self, name, description, vector_data=None):
        """
        Add a tool to the database.
        
        Args:
            name (str): Name of the tool.
            description (str): Description of the tool.
            vector_data (list, optional): Vector representation of the tool. Defaults to None.
        
        Returns:
            int: The ID of the inserted tool, or -1 if an error occurred.
        """
        if not self.conn:
            if not self.connect():
                return -1
        
        try:
            vector_json = json.dumps(vector_data) if vector_data else None
            self.cursor.execute(
                "INSERT INTO tools (name, description, vector_data) VALUES (?, ?, ?)",
                (name, description, vector_json)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding tool: {e}")
            return -1
    
    def get_tool(self, tool_id):
        """
        Get a tool from the database by ID.
        
        Args:
            tool_id (int): The ID of the tool to retrieve.
        
        Returns:
            dict: The tool data, or None if the tool was not found.
        """
        if not self.conn:
            if not self.connect():
                return None
        
        try:
            self.cursor.execute("SELECT * FROM tools WHERE id = ?", (tool_id,))
            row = self.cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "vector_data": json.loads(row[3]) if row[3] else None,
                    "created_at": row[4]
                }
            return None
        except sqlite3.Error as e:
            print(f"Error getting tool: {e}")
            return None
    
    def get_all_tools(self):
        """
        Get all tools from the database.
        
        Returns:
            list: A list of tool dictionaries.
        """
        if not self.conn:
            if not self.connect():
                return []
        
        try:
            self.cursor.execute("SELECT * FROM tools")
            rows = self.cursor.fetchall()
            tools = []
            for row in rows:
                tools.append({
                    "id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "vector_data": json.loads(row[3]) if row[3] else None,
                    "created_at": row[4]
                })
            return tools
        except sqlite3.Error as e:
            print(f"Error getting tools: {e}")
            return []
    
    def log_interaction(self, user_query, agent_response, tools_used=None):
        """
        Log an interaction with the agent.
        
        Args:
            user_query (str): The user's query.
            agent_response (str): The agent's response.
            tools_used (list, optional): List of tools used in the interaction. Defaults to None.
        
        Returns:
            int: The ID of the inserted log, or -1 if an error occurred.
        """
        if not self.conn:
            if not self.connect():
                return -1
        
        try:
            tools_json = json.dumps(tools_used) if tools_used else None
            self.cursor.execute(
                "INSERT INTO logs (user_query, agent_response, tools_used) VALUES (?, ?, ?)",
                (user_query, agent_response, tools_json)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error logging interaction: {e}")
            return -1
