# test_sdk.py
"""
Unit tests for the GAME SDK integration.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.sdk.sdk_api import GameSDKAPI

class TestGameSDKAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_api_key"
        self.sdk_api = GameSDKAPI(api_key=self.api_key)

    @patch("src.sdk.sdk_api.requests.post")
    def test_configure_agent(self, mock_post):
        # Mock API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        # Test configure_agent
        agent_id = "agent_123"
        configuration = {"strategy": "adaptive"}
        response = self.sdk_api.configure_agent(agent_id, configuration)

        self.assertEqual(response["status"], "success")
        mock_post.assert_called_once_with(
            f"https://api.gamesdk.com/v1/agents/{agent_id}/configure",
            headers=self.sdk_api._headers(),
            json=configuration,
        )

    @patch("src.sdk.sdk_api.requests.post")
    def test_add_function(self, mock_post):
        # Mock API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        # Test add_function
        agent_id = "agent_123"
        function_definition = {"name": "custom_function", "description": "Test function"}
        response = self.sdk_api.add_function(agent_id, function_definition)

        self.assertEqual(response["status"], "success")
        mock_post.assert_called_once_with(
            f"https://api.gamesdk.com/v1/agents/{agent_id}/functions",
            headers=self.sdk_api._headers(),
            json=function_definition,
        )

    @patch("src.sdk.sdk_api.requests.get")
    def test_get_agent_status(self, mock_get):
        # Mock API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "agent_status": "active"}
        mock_get.return_value = mock_response

        # Test get_agent_status
        agent_id = "agent_123"
        response = self.sdk_api.get_agent_status(agent_id)

        self.assertEqual(response["status"], "success")
        self.assertEqual(response["agent_status"], "active")
        mock_get.assert_called_once_with(
            f"https://api.gamesdk.com/v1/agents/{agent_id}/status",
            headers=self.sdk_api._headers(),
        )

if __name__ == "__main__":
    unittest.main()
