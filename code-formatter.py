
import sys
import tempfile
import os
import configparser


def replace_text(line, str_to_replace, replacement):
    length = len(str_to_replace)
    location = line.find(str_to_replace)

    edited_line = line[:location] + replacement + line[location + length:]
    return edited_line


def process_for(line, line_number, config):
    for_str = "for"
    location = line.find(for_str)

    for_bop_str = ""
    if config["white space"].getboolean("FOR_bop") is True:
        for_bop_str = " "

    for_aop_str = ""
    if config["white space"].getboolean("FOR_aop") is True:
        for_aop_str = " "

    correct_for = for_str + for_bop_str + "(" + for_aop_str

    print(line[location:location+len(correct_for)] + " : " + str(line_count))
    if line[location:location+len(correct_for)] == correct_for:
        return line

    if line[location - 1].isspace() is False:
        print("No space before for")
        return line

    # find opening paren
    i = location+len(for_str)
    for char in line[i:]:
        if char is "(":
            paren_start = i
            break

        if char.isspace() is False:
            return line

        i += 1

    for_statement = line[location:paren_start+1]

    print("Replaced for on line " + str(line_count))
    return replace_text(line, for_statement, correct_for)


# start of the main path of execution

if len(sys.argv) != 3:
    print("Usage: code-formatter.py <file name> <config file>")
    exit(1)

filename = sys.argv[1]
config_filename = sys.argv[2]

config = configparser.ConfigParser()
config.read(config_filename)

with open(filename, 'r') as file, tempfile.NamedTemporaryFile(mode='w', dir='.', delete=False) as fixed_file:

    line_count = 0
    for line in file:
        line_count += 1

        # Only operate on lines that have been modified
        if line[0] == "+":

            if "for" in line:
                fixed_file.write(process_for(line, line_count, config))
                continue

            if "if(" in line:
                fixed_line = replace_text(line, "if(", "if (")
                fixed_file.write(fixed_line)
                continue

            if "while(" in line:
                fixed_line = replace_text(line, "while(", "while (")
                fixed_file.write(fixed_line)
                continue

        fixed_file.write(line)

os.replace(fixed_file.name, filename)
