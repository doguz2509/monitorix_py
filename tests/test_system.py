"""Tests for system monitoring module."""

import pytest
from monitorix_py.lib.system import SystemMonitor


def test_system_monitor_init():
    """Test SystemMonitor initialization."""
    monitor = SystemMonitor()
    assert monitor is not None


def test_system_monitor_collect():
    """Test data collection."""
    monitor = SystemMonitor()
    stats = monitor.collect()
    
    # Check required keys
    assert 'timestamp' in stats
    assert 'hostname' in stats
    assert 'os' in stats
    assert 'cpu' in stats
    assert 'memory' in stats
    assert 'swap' in stats
    assert 'load' in stats
    assert 'uptime' in stats
    
    # Check CPU data
    assert 'percent' in stats['cpu']
    assert 'count' in stats['cpu']
    assert stats['cpu']['percent'] >= 0
    assert stats['cpu']['count'] > 0
    
    # Check memory data
    assert 'total' in stats['memory']
    assert 'used' in stats['memory']
    assert 'percent' in stats['memory']
    assert stats['memory']['total'] > 0
    assert 0 <= stats['memory']['percent'] <= 100


def test_system_monitor_format():
    """Test statistics formatting."""
    monitor = SystemMonitor()
    stats = monitor.collect()
    formatted = monitor.format_stats(stats)
    
    assert isinstance(formatted, str)
    assert len(formatted) > 0
    assert 'Hostname' in formatted
    assert 'CPU' in formatted
    assert 'Memory' in formatted
