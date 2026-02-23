import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower(): #ensure files are the same format
        sys.exit("Input and output have different extensions")
    else:
        shirt(sys.argv[1], sys.argv[2])


def shirt(x, y):
    try:
        with Image.open(x) as reference, Image.open("shirt.png") as shirt:
            fit_reference = ImageOps.fit(reference, shirt.size) #fit shirt to size of muppet
            fit_reference.paste(shirt, (0,0), shirt)
            fit_reference.save(y)
            # print(f"Reference size: {reference.size}")
            # print(f"Original shirt size: {shirt.size}")
            # print(f"Fitted shirt size: {fit_shirt.size}")
    except FileNotFoundError:
        sys.exit("File Not Found")


if __name__ == "__main__":
    main()
