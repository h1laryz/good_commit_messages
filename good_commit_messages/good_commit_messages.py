import sys
import re

COMMIT_MSG_PATTERN = r'^(feat|fix|style|refactor|test|docs|chore|ci|build|revert): .+'

def main():
    commit_msg_filepath = sys.argv[1]
    
    with open(commit_msg_filepath, 'r') as f:
        commit_msg = f.read()

    if not re.match(COMMIT_MSG_PATTERN, commit_msg):
        print(f"Commit message didn't pass regex: {COMMIT_MSG_PATTERN}")
        sys.exit(1)

if __name__ == '__main__':
    main()
