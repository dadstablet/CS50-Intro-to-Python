def convert(str):
    str.replace(":)", "🙂")
    str.replace(":(", "🙁")

def main():
    x = input("Input here: ")
    conv = convert(x)

main()
