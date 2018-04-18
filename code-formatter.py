import io
import sys

# start of the program

if len(sys.argv) < 2:
    print("Usage: code-formatter.py <patch name>")
    exit(1)

filename = sys.argv[1]

with open(filename, 'r+') as file:
    print(file.readline())
