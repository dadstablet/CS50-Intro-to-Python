import csv
import tabulate
import sys

def main():
    usr_input = sys.argv[:]
    if len(usr_input) > 2:
        sys.exit("Too many command-line argumets")
    elif len(usr_input) == 1:
        sys.exit("Too few command-line arguments")
    elif ".csv" not in usr_input[1]:
        sys.exit("Must be csv file")
    else:
        try:
            read_file(usr_input[1])
        except FileNotFoundError:
            sys.exit("File does not exist")

def read_file(x):
    with open(x, "r") as pizza:
        pizza = csv.DictReader(pizza)
        print(tabulate.tabulate(pizza, headers="keys", tablefmt="grid"))
        # for rows in pizza:
        #     print(rows)

if __name__ == "__main__":
    main()
