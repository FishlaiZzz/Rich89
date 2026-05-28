import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    # Run git log --all -p to get all history across all branches
    out = subprocess.check_output(['git', 'log', '--all', '-p', 'index.js']).decode('utf-8', errors='ignore')
    commits = out.split('commit ')
    print(f"Total commits scanned: {len(commits)}")
    
    found_any = False
    for commit in commits:
        if '佩婷' in commit:
            found_any = True
            lines = commit.splitlines()
            commit_id = lines[0] if lines else "Unknown"
            print(f"\n[Commit: {commit_id[:20]}]")
            for i, line in enumerate(lines):
                if '佩婷' in line or 'talent' in line:
                    start = max(0, i - 4)
                    end = min(len(lines), i + 5)
                    print('\n'.join(lines[start:end]))
                    print('-'*30)
    if not found_any:
        print("No references to '佩婷' found in git log --all.")
except Exception as e:
    print("Error:", e)
