"""Tests for process monitoring module."""

import pytest
from monitorix_py.lib.process import ProcessMonitor


def test_process_monitor_init():
    """Test ProcessMonitor initialization."""
    monitor = ProcessMonitor()
    assert monitor is not None


def test_process_monitor_collect():
    """Test data collection."""
    monitor = ProcessMonitor()
    stats = monitor.collect(top_n=5)
    
    # Check required keys
    assert 'timestamp' in stats
    assert 'count' in stats
    assert 'top_cpu' in stats
    assert 'top_memory' in stats
    assert 'threads' in stats
    
    # Check count data
    count = stats['count']
    assert 'total' in count
    assert 'running' in count
    assert 'sleeping' in count
    assert count['total'] > 0
    
    # Check top processes
    assert isinstance(stats['top_cpu'], list)
    assert isinstance(stats['top_memory'], list)
    assert len(stats['top_cpu']) <= 5
    assert len(stats['top_memory']) <= 5


def test_process_monitor_format():
    """Test statistics formatting."""
    monitor = ProcessMonitor()
    stats = monitor.collect()
    formatted = monitor.format_stats(stats)
    
    assert isinstance(formatted, str)
    assert len(formatted) > 0
    assert 'Process Statistics' in formatted
    assert 'Top Processes by CPU Usage' in formatted
    assert 'Top Processes by Memory Usage' in formatted
