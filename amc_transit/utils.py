"""
Utility functions for AMC Transit.
"""

import json
from typing import Any, Dict
from datetime import datetime


def format_timestamp(timestamp: int) -> str:
    """
    Format a Unix timestamp to a human-readable string.
    
    Args:
        timestamp: Unix timestamp in seconds
        
    Returns:
        Formatted datetime string
    """
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def save_to_json(data: Dict[str, Any], filename: str) -> None:
    """
    Save data to a JSON file.
    
    Args:
        data: Dictionary to save
        filename: Output filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_from_json(filename: str) -> Dict[str, Any]:
    """
    Load data from a JSON file.
    
    Args:
        filename: Input filename
        
    Returns:
        Dictionary loaded from the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_api_response(response: Dict[str, Any]) -> bool:
    """
    Validate that an API response has the expected structure.
    
    Args:
        response: API response dictionary
        
    Returns:
        True if valid, False otherwise
    """
    if not isinstance(response, dict):
        return False
    
    # Add more validation logic as needed
    return True
