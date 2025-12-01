def main():
    grocery_list = {}
    while True:
        try:
            x = input("input: ")
            grocery_list.append(x)
        except EOFError:
            break
    print(grocery_list)

main()
