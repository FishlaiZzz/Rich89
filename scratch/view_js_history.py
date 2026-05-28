import subprocess
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

try:
    # Get all commit hashes in history for index.js
    hashes = subprocess.check_output(['git', 'log', '--format=%H', 'index.js']).decode('utf-8').splitlines()
    print(f"Total commits for index.js: {len(hashes)}")
    
    for h in hashes:
        content = subprocess.check_output(['git', 'show', f'{h}:index.js']).decode('utf-8', errors='ignore')
        # Search for 王佩婷 block
        # Find where "王佩婷" appears and print the surrounding 10 lines
        lines = content.splitlines()
        for idx, line in enumerate(lines):
            if '王佩婷' in line:
                start = max(0, idx - 5)
                end = min(len(lines), idx + 6)
                # Get commit metadata
                info = subprocess.check_output(['git', 'show', '-s', '--format=%h - %s', h]).decode('utf-8').strip()
                print(f"\n[Commit: {info}]")
                print('\n'.join(lines[start:end]))
                print('-'*40)
except Exception as e:
    print("Error:", e)
