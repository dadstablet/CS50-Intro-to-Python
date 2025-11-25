def main():

    x = input("Input: ")
    vowels = "AEOUIaeoui"

    x_list = [char for char in x if char not in vowels]

    for char in x_list:
        print(char, end="")

main()
