# Tool Judge

import numpy as np
import re

class ToolJudge:
    """
    Class responsible for determining if a tool is needed based on the current hidden state.
    """
    
    def __init__(self, threshold=0.5):
        """
        Initialize the Tool Judge with a threshold.
        
        Args:
            threshold (float, optional): The threshold above which a tool is considered needed. Defaults to 0.5.
        """
        self.threshold = threshold
        # Keywords that suggest a tool might be needed
        self.tool_keywords = {
            # Weather-related keywords
            'weather': 0.8,
            'temperature': 0.75,
            'forecast': 0.85,
            'climate': 0.7,
            
            # Location/map keywords
            'location': 0.75,
            'capital': 0.9,
            'country': 0.7,
            'city': 0.65,
            
            # Calculation keywords
            'calculate': 0.95,
            'compute': 0.9,
            'solve': 0.8,
            'equation': 0.85,
            'formula': 0.85,
            
            # Translation keywords
            'translate': 0.95,
            'language': 0.75,
            'french': 0.7,
            'spanish': 0.7,
            'german': 0.7,
            
            # Web search keywords
            'search': 0.9,
            'find information': 0.85,
            'look up': 0.8,
            'find out': 0.75,
            
            # News-related keywords
            'news': 0.8,
            'recent': 0.7,
            'latest': 0.75,
            'current events': 0.9,
            
            # Web content keywords
            'website': 0.85,
            'webpage': 0.85,
            'url': 0.9,
            'link': 0.8,
            
            # Project file keywords
            'project file': 0.95,
            'project schedule': 0.95,
            'mpp': 0.95,
            'xer': 0.95,
            'critical path': 0.9,
            'tasks': 0.8,
            'resources': 0.8,
            'project management': 0.85
        }
    
    def check_tool_needed(self, hidden_state):
        """
        Determine if a tool is needed based on the hidden state.
        
        Args:
            hidden_state: The hidden state from the LLM.
        
        Returns:
            bool: True if a tool is needed, False otherwise.
        """
        score = self.calculate_score(hidden_state)
        return score > self.threshold
    
    def calculate_score(self, hidden_state):
        """
        Calculate the tool judge score based on the hidden state.
        
        Args:
            hidden_state: The hidden state from the LLM.
        
        Returns:
            float: The calculated score.
        """
        # In a real implementation, this would involve a neural network or other model
        # For this enhanced demo, we'll use a keyword-based approach with the simulated hidden state
        
        # For demonstration purposes, we'll convert the hidden state to a string if it's not already
        if not isinstance(hidden_state, str):
            # In a real implementation, we would process the actual hidden state
            # For demonstration, we'll just return a random score
            return np.random.uniform(0.0, 1.0)  # Random score for demonstration
        
        # Simple keyword matching (for demonstration purposes)
        content = hidden_state.lower()
        max_score = 0.0
        
        # Check for keywords
        for keyword, keyword_score in self.tool_keywords.items():
            if keyword.lower() in content:
                max_score = max(max_score, keyword_score)
        
        # Add some randomness for demonstration
        randomness = np.random.uniform(-0.1, 0.1)
        score = max(0.0, min(1.0, max_score + randomness))
        
        return score
