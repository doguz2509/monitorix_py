# Monitorix-py

A Python3 rewrite of [Monitorix](https://github.com/mikaku/Monitorix) - A lightweight system monitoring tool.

## About

Monitorix is a free, open-source, lightweight system monitoring tool designed to monitor as many services and system resources as possible. This project aims to rewrite the original Perl-based Monitorix in Python3 for better maintainability and modern development practices.

### Original Project

- **Original Author**: Jordi Sanfeliu
- **Original Project**: https://github.com/mikaku/Monitorix
- **License**: GNU General Public License v2

## Status

🚧 **Work in Progress** - This is an early-stage port from Perl to Python3.

### Currently Implemented

- ✅ Core package structure
- ✅ Configuration parser
- ✅ Main daemon with signal handling
- ✅ System monitoring module (CPU, memory, load, uptime)
- ✅ Basic utility functions

### Planned Features

- [ ] All 60+ monitoring modules from original Monitorix
- [ ] RRD database integration for metrics storage
- [ ] Built-in HTTP server for web interface
- [ ] CGI web interface
- [ ] Full configuration compatibility
- [ ] All graph types and visualizations

## Installation

### Requirements

- Python 3.8 or higher
- psutil library

### Install from Source

```bash
# Clone the repository
git clone https://github.com/doguz2509/monitorix_py.git
cd monitorix_py

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Usage

### Basic Usage

```bash
# Run with default configuration
monitorix

# Specify a configuration file
monitorix -c /path/to/monitorix.conf

# Show version
monitorix --version

# Enable debug mode
monitorix --debug
```

### Testing System Monitor

```python
from monitorix_py.lib.system import SystemMonitor

# Create monitor instance
monitor = SystemMonitor()

# Collect system statistics
stats = monitor.collect()

# Display formatted statistics
print(monitor.format_stats(stats))
```

## Development

### Setting Up Development Environment

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (when available)
pytest

# Format code
black monitorix_py/

# Lint code
ruff check monitorix_py/
```

### Project Structure

```
monitorix_py/
├── monitorix_py/           # Main package
│   ├── __init__.py         # Package initialization
│   ├── monitorix.py        # Main daemon entry point
│   └── lib/                # Monitoring modules
│       ├── __init__.py     # Core utilities
│       ├── config.py       # Configuration parser
│       └── system.py       # System monitoring module
├── pyproject.toml          # Package configuration
├── setup.py                # Setup script
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Contributing

Contributions are welcome! This is a large project with many modules to port from Perl to Python.

### Priority Modules to Port

1. File system monitoring (fs.pm)
2. Network monitoring (net.pm)
3. Disk I/O monitoring (disk.pm)
4. HTTP Server (HTTPServer.pm)
5. Web interface (monitorix.cgi)
6. Additional monitoring modules (50+ remaining)

## License

This project is licensed under the GNU General Public License v2, same as the original Monitorix project.

## Acknowledgments

- **Jordi Sanfeliu** - Original Monitorix creator
- Original Monitorix project and community
