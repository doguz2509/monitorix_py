# Monitorix-py Examples

This directory contains example scripts and configuration files for Monitorix-py.

## Files

### monitor_demo.py

A demonstration script that shows how to use all the monitoring modules:

```bash
# Run basic monitoring demo
python examples/monitor_demo.py

# Run with disk I/O rate calculation (waits 60 seconds)
python examples/monitor_demo.py --rates
```

### monitorix.conf

A sample configuration file showing the available options for Monitorix-py. This configuration format is compatible with the original Monitorix.

## Usage Examples

### Using Individual Monitoring Modules

```python
from monitorix_py.lib.system import SystemMonitor
from monitorix_py.lib.fs import FileSystemMonitor
from monitorix_py.lib.net import NetworkMonitor
from monitorix_py.lib.disk import DiskMonitor

# System monitoring
sys_monitor = SystemMonitor()
sys_stats = sys_monitor.collect()
print(sys_monitor.format_stats(sys_stats))

# Filesystem monitoring
fs_monitor = FileSystemMonitor()
fs_stats = fs_monitor.collect()
print(fs_monitor.format_stats(fs_stats))

# Network monitoring
net_monitor = NetworkMonitor()
net_stats = net_monitor.collect()
print(net_monitor.format_stats(net_stats))

# Disk monitoring
disk_monitor = DiskMonitor()
disk_stats = disk_monitor.collect()
print(disk_monitor.format_stats(disk_stats))
```

### Loading Configuration

```python
from monitorix_py.lib.config import load_config

# Load configuration file
config = load_config('examples/monitorix.conf')

# Access configuration values
title = config.get('title', 'Monitorix')
refresh_rate = config.get('refresh_rate', 60)

# Access nested configuration
system_enabled = config.get('system.enabled', True)
```

### Collecting Data Over Time

```python
import time
from monitorix_py.lib.disk import DiskMonitor

disk_monitor = DiskMonitor()

# Collect first snapshot
stats1 = disk_monitor.collect()

# Wait for interval
time.sleep(60)

# Collect second snapshot
stats2 = disk_monitor.collect()

# Calculate rates
rates = disk_monitor.calculate_rates(stats2, stats1, interval=60.0)
print(disk_monitor.format_stats(stats2, rates))
```

## Next Steps

- Explore additional monitoring modules as they are implemented
- Create custom monitoring scripts for your specific needs
- Integrate with your existing monitoring infrastructure
- Set up scheduled data collection with cron or systemd timers
