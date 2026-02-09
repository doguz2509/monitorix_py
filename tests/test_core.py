"""Tests for core utility functions."""

import pytest
from monitorix_py.lib import (
    logger,
    trim,
    min_val,
    max_val,
    celsius_to_fahrenheit,
    uptime_to_str,
    MonitorixError,
    ConfigError,
    DataCollectionError,
)


def test_trim():
    """Test trim function."""
    assert trim("  hello  ") == "hello"
    assert trim("hello") == "hello"
    assert trim("") == ""
    assert trim(None) is None


def test_min_val():
    """Test min_val function."""
    assert min_val(1, 2, 3) == 1
    assert min_val(5.5, 2.2, 3.3) == 2.2
    assert min_val(-1, 0, 1) == -1


def test_max_val():
    """Test max_val function."""
    assert max_val(1, 2, 3) == 3
    assert max_val(5.5, 2.2, 3.3) == 5.5
    assert max_val(-1, 0, 1) == 1


def test_celsius_to_fahrenheit():
    """Test temperature conversion."""
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert abs(celsius_to_fahrenheit(37) - 98.6) < 0.1


def test_uptime_to_str():
    """Test uptime formatting."""
    assert uptime_to_str(0) == "0m"
    assert uptime_to_str(60) == "1m"
    assert uptime_to_str(3600) == "1h"
    assert uptime_to_str(86400) == "1d"
    assert uptime_to_str(90061) == "1d 1h 1m"


def test_exceptions():
    """Test custom exceptions."""
    assert issubclass(ConfigError, MonitorixError)
    assert issubclass(DataCollectionError, MonitorixError)
    
    with pytest.raises(ConfigError):
        raise ConfigError("Test config error")
    
    with pytest.raises(DataCollectionError):
        raise DataCollectionError("Test data collection error")
