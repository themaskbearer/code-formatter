
import sys
import tempfile
import os


def replace_text(line, str_to_replace, replacement):
    length = len(str_to_replace)
    location = line.find(str_to_replace)

    edited_line = line[:location] + replacement + line[location + length:]
    return edited_line


# start of the main path of execution

if len(sys.argv) < 2:
    print("Usage: code-formatter.py <file name>")
    exit(1)

filename = sys.argv[1]

with open(filename, 'r') as file, tempfile.NamedTemporaryFile(mode='w', dir='.', delete=False) as fixed_file:

    for line in file:
        # Only operate on lines that have been modified
        if line[0] == "+":

            if "for(" in line:
                fixed_line = replace_text(line, "for(", "for (")
                fixed_file.write(fixed_line)
                continue

            if "if(" in line:
                fixed_line = replace_text(line, "if(", "if (")
                fixed_file.write(fixed_line)
                continue

        fixed_file.write(line)

os.replace(fixed_file.name, filename)
