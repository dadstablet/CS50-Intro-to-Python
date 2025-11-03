def convert(str):
    smile = str.replace(":)", "🙂")
    frown = str.replace(":(", "🙁")

def main():
    x = input("Input here: ")
    conv = convert(x)

main()
