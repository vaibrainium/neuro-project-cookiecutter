"""PRE gen hook
"""
import logging
import os
import shutil
import sys
import git 

_logger = logging.getLogger()
TMP_DIR = './tmp/' 

def pre_hook():
    """Flag the PRE gen HOOK execution"""
    _logger.warning("PRE Gen hook executed")

    try:
        None
               
    except OSError as e:
        _logger.warning(f"Error: {e}")
        sys.exit(0)

    # Exit with success
    sys.exit(0)

if __name__ == "__main__":
    pre_hook()