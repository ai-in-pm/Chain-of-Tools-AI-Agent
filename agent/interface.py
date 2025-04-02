# Interface for User Interaction

class UserInterface:
    """
    Class for managing user interaction, displaying query, thinking process, tool calls, and results.
    """
    
    def __init__(self):
        """
        Initialize the User Interface.
        """
        self.history = []
    
    def display_query(self, query):
        """
        Display the user's query.
        
        Args:
            query (str): The user's query.
        """
        print("\n" + "=" * 80)
        print(f"User Query: {query}")
        print("=" * 80)
        self.history.append({"type": "query", "content": query})
    
    def display_thinking(self, message):
        """
        Display the agent's thinking process.
        
        Args:
            message (str): The thinking message to display.
        """
        print(f"Thinking... {message}")
        self.history.append({"type": "thinking", "content": message})
    
    def display_tool_check(self, score):
        """
        Display the tool check result.
        
        Args:
            score (float): The tool judge score.
        """
        print(f"Tool Check: Score = {score:.2f}")
        self.history.append({"type": "tool_check", "content": score})
    
    def display_tool_selection(self, tool_name, description, score):
        """
        Display the selected tool.
        
        Args:
            tool_name (str): The name of the selected tool.
            description (str): The description of the selected tool.
            score (float): The similarity score.
        """
        print("\n" + "-" * 40)
        print(f"Selected Tool: {tool_name} (Score: {score:.2f})")
        print(f"Description: {description}")
        print("-" * 40)
        self.history.append({"type": "tool_selection", "content": {"name": tool_name, "description": description, "score": score}})
    
    def display_tool_call(self, tool_name, parameters):
        """
        Display the tool call with parameters.
        
        Args:
            tool_name (str): The name of the tool being called.
            parameters (dict): The parameters for the tool call.
        """
        param_str = ", ".join([f"{k}={v}" for k, v in parameters.items()])
        print(f"Calling: {tool_name}({param_str})")
        self.history.append({"type": "tool_call", "content": {"name": tool_name, "parameters": parameters}})
    
    def display_tool_result(self, tool_name, result):
        """
        Display the result of a tool call.
        
        Args:
            tool_name (str): The name of the tool that was called.
            result: The result of the tool call.
        """
        print(f"\nResult from {tool_name}:\n")
        
        # Format display based on tool type
        if tool_name in ["WebSearch", "NewsSearch"]:
            # For search results, display with proper formatting
            print("-" * 70)
            print(result)
            print("-" * 70)
        elif tool_name == "WebContentFetcher":
            # For web content, display a snippet
            print("-" * 70)
            lines = result.split('\n')
            if len(lines) > 10:
                # Show first few lines with ellipsis
                print('\n'.join(lines[:10]))
                print("...")
                print(f"[Content truncated, total length: {len(result)} characters]")
            else:
                print(result)
            print("-" * 70)
        else:
            # For other tools, display normally
            print(result)
            
        self.history.append({"type": "tool_result", "content": {"name": tool_name, "result": result}})
    
    def display_token_generation(self, token):
        """
        Display a generated token.
        
        Args:
            token (str): The generated token.
        """
        print(token, end="", flush=True)
        self.history.append({"type": "token", "content": token})
    
    def display_result(self, result):
        """
        Display the final result.
        
        Args:
            result (str): The final result to display.
        """
        print("\n" + "=" * 80)
        print("Final Answer:")
        print(result)
        print("=" * 80)
        self.history.append({"type": "result", "content": result})
    
    def get_history(self):
        """
        Get the interaction history.
        
        Returns:
            list: The interaction history.
        """
        return self.history
