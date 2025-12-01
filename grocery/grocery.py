def main():
    user_list = {}
    while True:
        try:
            x = input("input: ")
            user_list.append(x)
        except EOFError:
            break
    print(grocery_list)

main()
