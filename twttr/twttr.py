def main():

    x = input("Input: ")
    vowels = "AEOUIaeoui"

    x_list = [char for char in x if char not in vowels]
    print(str(x_list))

main()
