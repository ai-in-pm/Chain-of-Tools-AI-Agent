# Tool implementations for the AI Agent

class WeatherAPI:
    """
    Tool for getting weather information for a location.
    """
    
    @staticmethod
    def get_weather(location, date=None):
        """
        Get weather information for a location and date.
        
        Args:
            location (str): The location to get weather for.
            date (str, optional): The date to get weather for. Defaults to None (current date).
        
        Returns:
            str: The weather information.
        """
        # In a real implementation, this would call an actual weather API
        if not date or date == "yesterday":
            return f"Weather in {location} yesterday: Cloudy, 65°F"
        elif date == "today":
            return f"Weather in {location} today: Sunny, 72°F"
        else:
            return f"Weather in {location} on {date}: Data not available"


class CapitalAPI:
    """
    Tool for finding the capital city of a country.
    """
    
    # Sample data for demonstration
    CAPITALS = {
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
        "spain": "Madrid",
        "united kingdom": "London",
        "usa": "Washington D.C.",
        "canada": "Ottawa",
        "japan": "Tokyo",
        "china": "Beijing",
        "australia": "Canberra"
    }
    
    @staticmethod
    def get_capital(country):
        """
        Get the capital city of a country.
        
        Args:
            country (str): The country to get the capital of.
        
        Returns:
            str: The capital city.
        """
        country = country.lower()
        if country in CapitalAPI.CAPITALS:
            return f"The capital of {country.title()} is {CapitalAPI.CAPITALS[country]}"
        else:
            return f"Capital information for {country.title()} not found"


class SearchAPI:
    """
    Tool for searching for information on the web.
    """
    
    @staticmethod
    def search(query):
        """
        Search for information on the web.
        
        Args:
            query (str): The search query.
        
        Returns:
            str: The search results.
        """
        # In a real implementation, this would call an actual search API
        return f"Search results for '{query}': Found relevant information about {query}."


class CalculatorAPI:
    """
    Tool for performing mathematical calculations.
    """
    
    @staticmethod
    def calculate(expression):
        """
        Perform a mathematical calculation.
        
        Args:
            expression (str): The mathematical expression to evaluate.
        
        Returns:
            str: The calculation result.
        """
        try:
            # Warning: eval can be dangerous in production code
            # This is just for demonstration purposes
            result = eval(expression)
            return f"Calculation result: {expression} = {result}"
        except Exception as e:
            return f"Error calculating {expression}: {str(e)}"


class TranslateAPI:
    """
    Tool for translating text from one language to another.
    """
    
    @staticmethod
    def translate(text, source_lang, target_lang):
        """
        Translate text from one language to another.
        
        Args:
            text (str): The text to translate.
            source_lang (str): The source language code.
            target_lang (str): The target language code.
        
        Returns:
            str: The translated text.
        """
        # In a real implementation, this would call an actual translation API
        return f"Translation of '{text}' from {source_lang} to {target_lang}: [translated text would appear here]"
