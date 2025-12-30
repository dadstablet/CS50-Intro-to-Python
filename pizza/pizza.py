import csv
import tabulate

def main():
    with open("sicilian.csv", "r") as sicilian, open("regular.csv", "r") as regular:
        sicilian = csv.DictReader(sicilian)
        regular = csv.DictReader(regular)

        print(tabulate.tabulate(sicilian))

if __name__ == "__main__":
    main()
