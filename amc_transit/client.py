"""
Main client module for interacting with transit APIs.
"""

import requests
from typing import Dict, Optional, Any
import json


class TransitClient:
    """
    Main client for retrieving data from transit APIs.
    
    This class provides methods to interact with various transit data sources
    and APIs. It can be extended to support multiple transit systems.
    """
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the TransitClient.
        
        Args:
            api_key: Optional API key for authentication
            base_url: Optional base URL for the transit API
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        
        if self.api_key:
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})
    
    def get_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieve data from a transit API endpoint.
        
        Args:
            endpoint: API endpoint to query
            params: Optional query parameters
            
        Returns:
            Dictionary containing the API response data
            
        Raises:
            requests.RequestException: If the API request fails
        """
        if not self.base_url:
            raise ValueError("Base URL must be set to retrieve data")
        
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error retrieving data from {url}: {str(e)}")
    
    def get_routes(self, **kwargs) -> Dict[str, Any]:
        """
        Retrieve transit routes.
        
        Args:
            **kwargs: Optional parameters for filtering routes
            
        Returns:
            Dictionary containing route information
        """
        return self.get_data("routes", params=kwargs)
    
    def get_stops(self, **kwargs) -> Dict[str, Any]:
        """
        Retrieve transit stops.
        
        Args:
            **kwargs: Optional parameters for filtering stops
            
        Returns:
            Dictionary containing stop information
        """
        return self.get_data("stops", params=kwargs)
    
    def get_arrivals(self, stop_id: str, **kwargs) -> Dict[str, Any]:
        """
        Retrieve arrival predictions for a specific stop.
        
        Args:
            stop_id: ID of the transit stop
            **kwargs: Optional parameters
            
        Returns:
            Dictionary containing arrival predictions
        """
        endpoint = f"stops/{stop_id}/arrivals"
        return self.get_data(endpoint, params=kwargs)
    
    def close(self):
        """Close the HTTP session."""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
