#!/usr/bin/env python3
"""
Example script demonstrating Monitorix-py monitoring modules.

This script shows how to use the various monitoring modules to collect
system statistics.
"""

import sys
import time
from datetime import datetime

from monitorix_py.lib.system import SystemMonitor
from monitorix_py.lib.fs import FileSystemMonitor
from monitorix_py.lib.net import NetworkMonitor
from monitorix_py.lib.disk import DiskMonitor


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)


def main():
    """Main function to demonstrate monitoring capabilities."""
    print(f"Monitorix-py Monitoring Demo")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # System monitoring
        print_header("SYSTEM STATISTICS")
        sys_monitor = SystemMonitor()
        sys_stats = sys_monitor.collect()
        print(sys_monitor.format_stats(sys_stats))
        
        # Filesystem monitoring
        print_header("FILESYSTEM STATISTICS")
        fs_monitor = FileSystemMonitor()
        fs_stats = fs_monitor.collect()
        print(fs_monitor.format_stats(fs_stats))
        
        # Network monitoring
        print_header("NETWORK STATISTICS")
        net_monitor = NetworkMonitor()
        net_stats = net_monitor.collect()
        print(net_monitor.format_stats(net_stats))
        
        # Disk monitoring
        print_header("DISK I/O STATISTICS")
        disk_monitor = DiskMonitor()
        disk_stats = disk_monitor.collect()
        print(disk_monitor.format_stats(disk_stats))
        
        # Demonstrate rate calculation for disk I/O
        if len(sys.argv) > 1 and sys.argv[1] == '--rates':
            print_header("DISK I/O RATES (60 second interval)")
            print("Waiting 60 seconds...")
            time.sleep(60)
            
            disk_stats2 = disk_monitor.collect()
            rates = disk_monitor.calculate_rates(disk_stats2, disk_stats, interval=60.0)
            print(disk_monitor.format_stats(disk_stats2, rates))
        
        print("\n" + "=" * 80)
        print("Monitoring complete!")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
