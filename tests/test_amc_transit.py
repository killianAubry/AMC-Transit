"""
Unit tests for AMC Transit.
"""

import unittest
from unittest.mock import Mock, patch
from amc_transit.client import TransitClient
from amc_transit.utils import format_timestamp, validate_api_response


class TestTransitClient(unittest.TestCase):
    """Test cases for the TransitClient class."""
    
    def test_client_initialization(self):
        """Test that TransitClient initializes correctly."""
        client = TransitClient()
        self.assertIsNone(client.api_key)
        self.assertIsNone(client.base_url)
        self.assertIsNotNone(client.session)
    
    def test_client_with_api_key(self):
        """Test TransitClient initialization with API key."""
        api_key = "test_key"
        client = TransitClient(api_key=api_key)
        self.assertEqual(client.api_key, api_key)
        self.assertIn('Authorization', client.session.headers)
    
    def test_client_with_base_url(self):
        """Test TransitClient initialization with base URL."""
        base_url = "https://api.example.com"
        client = TransitClient(base_url=base_url)
        self.assertEqual(client.base_url, base_url)
    
    def test_get_data_without_base_url(self):
        """Test that get_data raises error without base URL."""
        client = TransitClient()
        with self.assertRaises(ValueError):
            client.get_data("routes")
    
    def test_context_manager(self):
        """Test TransitClient works as context manager."""
        with TransitClient() as client:
            self.assertIsNotNone(client)
    
    @patch('amc_transit.client.requests.Session.get')
    def test_get_routes(self, mock_get):
        """Test get_routes method."""
        mock_response = Mock()
        mock_response.json.return_value = {"routes": []}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        client = TransitClient(base_url="https://api.example.com")
        result = client.get_routes()
        
        self.assertIn("routes", result)
        mock_get.assert_called_once()


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_format_timestamp(self):
        """Test timestamp formatting."""
        timestamp = 1698000000
        formatted = format_timestamp(timestamp)
        self.assertIsInstance(formatted, str)
        self.assertIn("2023", formatted)
    
    def test_validate_api_response_with_dict(self):
        """Test API response validation with dictionary."""
        response = {"data": "test"}
        self.assertTrue(validate_api_response(response))
    
    def test_validate_api_response_with_non_dict(self):
        """Test API response validation with non-dictionary."""
        response = "not a dict"
        self.assertFalse(validate_api_response(response))


if __name__ == '__main__':
    unittest.main()
