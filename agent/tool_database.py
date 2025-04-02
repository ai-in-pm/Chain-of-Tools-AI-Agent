# Tool Database Module

import json
import os
import numpy as np
from agent.database import AgentDatabase

class ToolDatabase:
    """
    Class for managing the tool database, including tool descriptions and vectors.
    """
    
    def __init__(self, db_path, tool_encoder=None):
        """
        Initialize the tool database with the given path and tool encoder.
        
        Args:
            db_path (str): Path to the database file.
            tool_encoder: Tool encoder instance for computing tool vectors.
        """
        self.db = AgentDatabase(db_path)
        self.tool_encoder = tool_encoder
        self.tools = {}
        self.tool_vectors = {}
    
    def initialize(self):
        """
        Initialize the tool database by loading tools from the database.
        
        Returns:
            bool: True if initialization successful, False otherwise.
        """
        try:
            # Initialize the database tables
            self.db.initialize_database()
            
            # Load tools from the database
            tools = self.db.get_all_tools()
            for tool in tools:
                self.tools[tool["id"]] = {
                    "name": tool["name"],
                    "description": tool["description"]
                }
                if tool["vector_data"]:
                    self.tool_vectors[tool["id"]] = tool["vector_data"]
            
            # If there are no tools in the database, add some sample tools
            if not self.tools:
                self._add_sample_tools()
            
            return True
        except Exception as e:
            print(f"Tool database initialization warning: {e}. Using default tools.")
            # Add sample tools in memory even if database fails
            self._add_sample_tools_in_memory()
            return True
    
    def _add_sample_tools(self):
        """
        Add sample tools to the database for demonstration purposes.
        """
        sample_tools = [
            {
                "name": "WeatherAPI",
                "description": "Get current weather information for a location."
            },
            {
                "name": "CapitalAPI",
                "description": "Find the capital city of a country."
            },
            {
                "name": "SearchAPI",
                "description": "Search for information on the web."
            },
            {
                "name": "CalculatorAPI",
                "description": "Perform mathematical calculations."
            },
            {
                "name": "TranslateAPI",
                "description": "Translate text from one language to another."
            }
        ]
        
        for tool in sample_tools:
            vector_data = None
            if self.tool_encoder:
                vector_data = self.tool_encoder.encode(tool["description"])
            
            tool_id = self.db.add_tool(tool["name"], tool["description"], vector_data)
            if tool_id != -1:
                self.tools[tool_id] = {
                    "name": tool["name"],
                    "description": tool["description"]
                }
                if vector_data:
                    self.tool_vectors[tool_id] = vector_data
    
    def _add_sample_tools_in_memory(self):
        """
        Add sample tools to memory for demonstration purposes when database fails.
        """
        sample_tools = [
            {
                "name": "WeatherAPI",
                "description": "Get current weather information for a location."
            },
            {
                "name": "CapitalAPI",
                "description": "Find the capital city of a country."
            },
            {
                "name": "SearchAPI",
                "description": "Search for information on the web."
            },
            {
                "name": "CalculatorAPI",
                "description": "Perform mathematical calculations."
            },
            {
                "name": "TranslateAPI",
                "description": "Translate text from one language to another."
            },
            {
                "name": "WebSearch",
                "description": "Search the web for information."
            },
            {
                "name": "NewsSearch",
                "description": "Search for news articles with date filtering."
            },
            {
                "name": "WebContentFetcher",
                "description": "Fetch content from a URL."
            },
            {
                "name": "ProjectFileProcessor",
                "description": "Process and analyze project management files."
            }
        ]
        
        for i, tool in enumerate(sample_tools):
            self.tools[i+1] = {
                "name": tool["name"],
                "description": tool["description"]
            }
            # Generate random vector for demo purposes
            if self.tool_encoder:
                try:
                    vector = self.tool_encoder.encode(tool["description"])
                    self.tool_vectors[i+1] = vector
                except:
                    # If encoding fails, use random vector
                    self.tool_vectors[i+1] = np.random.randn(768).tolist()
            else:
                # If no encoder, use random vector
                self.tool_vectors[i+1] = np.random.randn(768).tolist()
    
    def get_tool(self, tool_id):
        """
        Get a tool by ID.
        
        Args:
            tool_id: The ID of the tool to retrieve.
        
        Returns:
            dict: The tool data, or None if the tool was not found.
        """
        return self.tools.get(tool_id)
    
    def get_tool_vector(self, tool_id):
        """
        Get a tool's vector by ID.
        
        Args:
            tool_id: The ID of the tool to retrieve the vector for.
        
        Returns:
            list: The tool vector, or None if the tool or vector was not found.
        """
        return self.tool_vectors.get(tool_id)
    
    def compute_tool_vectors(self):
        """
        Compute vectors for all tools using the tool encoder.
        
        Returns:
            bool: True if computation successful, False otherwise.
        """
        if not self.tool_encoder:
            return False
        
        for tool_id, tool in self.tools.items():
            vector = self.tool_encoder.encode(tool["description"])
            self.tool_vectors[tool_id] = vector
            
            # Update the vector in the database
            self.db.cursor.execute(
                "UPDATE tools SET vector_data = ? WHERE id = ?",
                (json.dumps(vector), tool_id)
            )
        
        self.db.conn.commit()
        return True
    
    def find_similar_tool(self, query_vector):
        """
        Find the most similar tool to the given query vector.
        
        Args:
            query_vector (list): The query vector to find similar tools for.
        
        Returns:
            tuple: (tool_id, score) of the most similar tool, or (None, 0) if no tools are found.
        """
        if not self.tool_vectors:
            return None, 0
        
        max_score = -1
        max_tool_id = None
        
        for tool_id, tool_vector in self.tool_vectors.items():
            # Calculate dot product similarity
            score = self._dot_product(query_vector, tool_vector)
            
            if score > max_score:
                max_score = score
                max_tool_id = tool_id
        
        return max_tool_id, max_score
    
    def _dot_product(self, vec1, vec2):
        """
        Calculate the dot product of two vectors.
        
        Args:
            vec1 (list): First vector.
            vec2 (list): Second vector.
        
        Returns:
            float: Dot product of the two vectors.
        """
        return sum(a * b for a, b in zip(vec1, vec2))
