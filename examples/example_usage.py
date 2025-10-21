"""
Example script demonstrating how to use the AMC Transit library.

This example shows how to create a TransitClient and retrieve data from a transit API.
Note: You'll need to configure the base_url and api_key for your specific transit API.
"""

from amc_transit import TransitClient
from amc_transit.utils import save_to_json, format_timestamp
import os


def example_basic_usage():
    """
    Basic example of using the TransitClient.
    """
    print("AMC Transit - Example Usage")
    print("=" * 50)
    
    # Example 1: Create a client (without API credentials for demonstration)
    print("\n1. Creating a TransitClient...")
    
    # In real usage, you would provide your API credentials:
    # api_key = os.getenv('TRANSIT_API_KEY')
    # base_url = 'https://api.transit-system.com/v1'
    # client = TransitClient(api_key=api_key, base_url=base_url)
    
    client = TransitClient()
    print("   Client created successfully!")
    
    # Example 2: Using context manager
    print("\n2. Using TransitClient as a context manager...")
    with TransitClient() as client:
        print("   Client will automatically close when done")
    
    # Example 3: Demonstrate expected usage (will fail without real API)
    print("\n3. Example API calls (requires configuration):")
    print("   - To get routes: client.get_routes()")
    print("   - To get stops: client.get_stops()")
    print("   - To get arrivals: client.get_arrivals(stop_id='123')")
    
    print("\n" + "=" * 50)
    print("To use this library with a real transit API:")
    print("1. Set your API credentials:")
    print("   export TRANSIT_API_KEY='your-api-key'")
    print("2. Configure the base URL for your transit API")
    print("3. Use the client methods to retrieve data")
    print("=" * 50)


def example_with_mock_data():
    """
    Example using mock data to demonstrate the utility functions.
    """
    print("\n\nUtility Functions Example")
    print("=" * 50)
    
    # Mock transit data
    mock_data = {
        "routes": [
            {"id": "1", "name": "Route 1", "type": "bus"},
            {"id": "2", "name": "Route 2", "type": "train"}
        ],
        "timestamp": 1698000000
    }
    
    # Save to JSON
    output_file = "/tmp/transit_data.json"
    save_to_json(mock_data, output_file)
    print(f"\nSaved mock data to {output_file}")
    
    # Format timestamp
    from amc_transit.utils import format_timestamp
    formatted_time = format_timestamp(mock_data["timestamp"])
    print(f"Formatted timestamp: {formatted_time}")
    
    print("=" * 50)


if __name__ == "__main__":
    example_basic_usage()
    example_with_mock_data()
