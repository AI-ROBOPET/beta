# sdk_api.py
"""
Integration module for the GAME SDK.
Provides utilities to communicate with the GAME SDK API.
"""

import requests

class GameSDKAPI:
    BASE_URL = "https://api.gamesdk.com/v1"

    def __init__(self, api_key):
        """
        Initialize the SDK API client.
        
        :param api_key: API key for authentication
        """
        self.api_key = api_key

    def _headers(self):
        """
        Generate request headers for authentication.
        
        :return: Dictionary of headers
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def configure_agent(self, agent_id, configuration):
        """
        Configure an AI agent with specific settings.
        
        :param agent_id: ID of the agent to configure
        :param configuration: Dictionary of configuration options
        :return: Response from the API
        """
        url = f"{self.BASE_URL}/agents/{agent_id}/configure"
        response = requests.post(url, headers=self._headers(), json=configuration)
        return response.json()

    def add_function(self, agent_id, function_definition):
        """
        Add a custom function to an agent.
        
        :param agent_id: ID of the agent
        :param function_definition: Dictionary defining the custom function
        :return: Response from the API
        """
        url = f"{self.BASE_URL}/agents/{agent_id}/functions"
        response = requests.post(url, headers=self._headers(), json=function_definition)
        return response.json()

    def get_agent_status(self, agent_id):
        """
        Retrieve the current status of an AI agent.
        
        :param agent_id: ID of the agent
        :return: Response from the API
        """
        url = f"{self.BASE_URL}/agents/{agent_id}/status"
        response = requests.get(url, headers=self._headers())
        return response.json()
