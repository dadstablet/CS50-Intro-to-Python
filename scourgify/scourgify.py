import sys
import csv

def main():
    x = sys.argv[:]
    if len(x) > 3:
        sys.exit("Too many command-line arguments")
    elif len(x) < 3:
        sys.exit("Too few command-line arguments")
    else:
        file_input = x[1]
        file_output = x[2]
    try:
        scourgify(file_input, file_output)
    except FileNotFoundError:
        sys.exit("File does not Exist")

def scourgify(x, y):
    with open(x, "r") as r, open(y, "w") as w:
        reader = csv.DictReader(r)
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(w, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            # first_name = name.split(",")[0]
            # last_name = name.split(",")[1]
            name = row["name"]
            house = row["house"]
            writer.writerow({"first": name.split(",")[1].strip(), "last": name.split(",")[0].strip(), "house": house})


if __name__ == "__main__":
    main()
