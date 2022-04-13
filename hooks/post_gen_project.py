"""POST gen hook
"""
import logging
import os
import shutil
import sys
from distutils.dir_util import copy_tree
import subprocess


_logger = logging.getLogger()
TMP_DIR = './tmp/' 

def post_hook():
    """Flag the POST gen HOOK execution"""
    _logger.warning("POST Gen hook executed")

    try:
    	None
		# subprocess.call(['git', 'init'])
		# subprocess.call(['git', 'add', '*'])
		# subprocess.call(['git', 'commit', '-m', 'Initial commit'])

    except OSError as e:
        #_logger.warning("While attempting to remove file(s) an error occurred")
        _logger.warning(f"Error: {e}")
        sys.exit(0)

    # Exit with success     
    sys.exit(0)

if __name__ == "__main__":
    post_hook()