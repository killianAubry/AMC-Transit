# AMC Transit

Python scripts to retrieve data from transit APIs and data sources.

## Overview

AMC Transit is a collection of Python scripts designed to fetch and process data from various transit APIs and data sources. This project provides a simple and extensible framework for working with transit data.

## Features

- Retrieve real-time transit data from various APIs
- Modular design for easy integration of new data sources
- Built with Python best practices
- Easy to use and extend

## Installation

### Using pip

```bash
pip install -r requirements.txt
```

### From source

```bash
git clone https://github.com/killianAubry/AMC-Transit.git
cd AMC-Transit
pip install -e .
```

## Usage

### Basic Example

```python
from amc_transit.client import TransitClient

# Create a transit client
client = TransitClient()

# Example usage will be added as data sources are implemented
```

## Project Structure

```
AMC-Transit/
├── amc_transit/          # Main package directory
│   ├── __init__.py       # Package initialization
│   ├── client.py         # Main client for transit APIs
│   └── utils.py          # Utility functions
├── examples/             # Example scripts
│   └── example_usage.py  # Example usage script
├── tests/                # Test directory
├── requirements.txt      # Project dependencies
├── setup.py              # Package setup configuration
└── README.md            # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Contact

For questions or support, please open an issue on GitHub.