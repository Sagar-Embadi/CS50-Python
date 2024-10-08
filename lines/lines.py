import sys


def main():
    # check the command line arguments
    check_command_line_arg()
    # try to open file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    # if it can't open then the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # loop through the lines and check if starts with # or Whitespace
    count_lines = 0
    for line in lines:
        if check_comment_or_empty_line(line) == False:
            count_lines +=1
    print(count_lines)

def check_command_line_arg():
    # check how many elements in the command lne
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # check if it is python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_comment_or_empty_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()
