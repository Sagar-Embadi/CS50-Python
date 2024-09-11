import sys
import csv
from tabulate import tabulate

def main():
    check_command_line_arg()
    table = []
    # try to open file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    # if can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # print the table
    print(tabulate(table[1:], headers = table[0], tablefmt="grid"))

def check_command_line_arg():
    # check how many elements in the command lne
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # check if it is csv file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
