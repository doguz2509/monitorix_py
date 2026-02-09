#!/usr/bin/env python3
"""
Monitorix - A lightweight system monitoring tool (Python3 rewrite).

This is the main entry point for the Monitorix monitoring daemon.

Copyright (C) 2005-2022 by Jordi Sanfeliu <jordi@fibranet.cat> (original Perl version)
Copyright (C) 2024 Monitorix Python Port Team (Python3 rewrite)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""

import argparse
import os
import signal
import sys
import time
from pathlib import Path
from typing import Optional

from .lib import logger, ConfigError

VERSION = "0.1.0"
RELEASE_DATE = "09-Feb-2024"


class Monitorix:
    """Main Monitorix daemon class."""
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize Monitorix daemon.
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file or "/etc/monitorix/monitorix.conf"
        self.config = {}
        self.running = False
        self.pid_file = "/var/run/monitorix.pid"
        
    def load_config(self) -> None:
        """Load and parse configuration file."""
        logger(f"Loading configuration from {self.config_file}")
        
        if not os.path.exists(self.config_file):
            raise ConfigError(f"Configuration file not found: {self.config_file}")
        
        # TODO: Implement full configuration parser
        # For now, just check that the file exists
        logger("Configuration loaded successfully")
        
    def setup_signal_handlers(self) -> None:
        """Set up signal handlers for graceful shutdown."""
        def signal_handler(signum, frame):
            logger(f"Received signal {signum}, shutting down...")
            self.running = False
            
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGQUIT, signal_handler)
        
    def write_pid_file(self) -> None:
        """Write process ID to PID file."""
        try:
            pid_dir = os.path.dirname(self.pid_file)
            if not os.path.exists(pid_dir):
                os.makedirs(pid_dir, exist_ok=True)
            
            with open(self.pid_file, 'w') as f:
                f.write(str(os.getpid()))
            logger(f"PID file created: {self.pid_file}")
        except Exception as e:
            logger(f"Warning: Could not create PID file: {e}")
            
    def remove_pid_file(self) -> None:
        """Remove PID file."""
        try:
            if os.path.exists(self.pid_file):
                os.remove(self.pid_file)
                logger(f"PID file removed: {self.pid_file}")
        except Exception as e:
            logger(f"Warning: Could not remove PID file: {e}")
            
    def run(self) -> None:
        """Run the main monitoring loop."""
        logger(f"Monitorix v{VERSION} starting...")
        logger(f"Release date: {RELEASE_DATE}")
        
        try:
            self.load_config()
            self.setup_signal_handlers()
            self.write_pid_file()
            
            self.running = True
            logger("Monitoring daemon started")
            
            # Main monitoring loop
            while self.running:
                # TODO: Implement actual monitoring logic
                # For now, just sleep
                time.sleep(60)
                
        except KeyboardInterrupt:
            logger("Interrupted by user")
        except Exception as e:
            logger(f"Error: {e}")
            raise
        finally:
            self.remove_pid_file()
            logger("Monitorix daemon stopped")


def main() -> int:
    """
    Main entry point for the Monitorix daemon.
    
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parser = argparse.ArgumentParser(
        description="Monitorix - A lightweight system monitoring tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        "-c", "--config",
        metavar="FILE",
        help="specify configuration file (default: /etc/monitorix/monitorix.conf)"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"Monitorix v{VERSION} ({RELEASE_DATE})"
    )
    
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="enable debug mode"
    )
    
    parser.add_argument(
        "-p", "--pidfile",
        metavar="FILE",
        help="specify PID file location (default: /var/run/monitorix.pid)"
    )
    
    args = parser.parse_args()
    
    try:
        daemon = Monitorix(config_file=args.config)
        if args.pidfile:
            daemon.pid_file = args.pidfile
        daemon.run()
        return 0
    except ConfigError as e:
        logger(f"Configuration error: {e}")
        return 1
    except Exception as e:
        logger(f"Fatal error: {e}")
        if args.debug:
            raise
        return 1


if __name__ == "__main__":
    sys.exit(main())
