# Tool Encoder

import numpy as np

class ToolEncoder:
    """
    Class for encoding tool descriptions into vector representations for similarity comparison.
    """
    
    def __init__(self, embedding_dim=768):
        """
        Initialize the Tool Encoder with the specified embedding dimension.
        
        Args:
            embedding_dim (int, optional): Dimension of the embedding vectors. Defaults to 768.
        """
        self.embedding_dim = embedding_dim
    
    def encode(self, tool_description):
        """
        Encode the tool description into a vector representation.
        
        Args:
            tool_description (str): The tool description to encode.
        
        Returns:
            list: The encoded tool vector.
        """
        # In a real implementation, this would use a pretrained model to encode the description
        # For demonstration purposes, we're generating a random vector
        vector = np.random.randn(self.embedding_dim)
        # Normalize the vector
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        
        return vector.tolist()
    
    def batch_encode(self, descriptions):
        """
        Encode multiple tool descriptions into vector representations.
        
        Args:
            descriptions (list): List of tool descriptions to encode.
        
        Returns:
            list: List of encoded tool vectors.
        """
        return [self.encode(desc) for desc in descriptions]
    
    def encode_tools(self, tools):
        """
        Encode a dictionary of tools into vector representations.
        
        Args:
            tools (dict): Dictionary mapping tool IDs to tool data with 'description' keys.
        
        Returns:
            dict: Dictionary mapping tool IDs to encoded vectors.
        """
        tool_vectors = {}
        for tool_id, tool_data in tools.items():
            if 'description' in tool_data:
                tool_vectors[tool_id] = self.encode(tool_data['description'])
        
        return tool_vectors
