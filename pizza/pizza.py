import csv
import tabulate
import sys

def main():
    usr_input = sys.argv[:]
    if len(usr_input) > 2:
        sys.exit("Too many command-line argumets")
    elif len(usr_input) == 1:
        sys.exit("Too few command-line arguments")
    else:
        try:
            read_file(usr_input)
        except 


def read_file(x):
    with open("sicilian.csv", "r") as sicilian, open("regular.csv", "r") as regular:
        sicilian = csv.DictReader(sicilian)
        regular = csv.DictReader(regular)

        print(tabulate.tabulate(sicilian))

if __name__ == "__main__":
    main()
