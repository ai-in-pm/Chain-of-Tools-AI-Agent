# Query Encoder

import numpy as np

class QueryEncoder:
    """
    Class for encoding queries into vector representations for similarity comparison.
    """
    
    def __init__(self, embedding_dim=768):
        """
        Initialize the Query Encoder with the specified embedding dimension.
        
        Args:
            embedding_dim (int, optional): Dimension of the embedding vectors. Defaults to 768.
        """
        self.embedding_dim = embedding_dim
    
    def encode(self, query):
        """
        Encode the query into a vector representation.
        
        Args:
            query (str): The query to encode.
        
        Returns:
            list: The encoded query vector.
        """
        # In a real implementation, this would use a pretrained model to encode the query
        # For demonstration purposes, we're generating a random vector
        vector = np.random.randn(self.embedding_dim)
        # Normalize the vector
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        
        return vector.tolist()
    
    def batch_encode(self, queries):
        """
        Encode multiple queries into vector representations.
        
        Args:
            queries (list): List of queries to encode.
        
        Returns:
            list: List of encoded query vectors.
        """
        return [self.encode(query) for query in queries]
