def main():
    user_list = {}
    while True:
        try:
            x = input("input: ")
            user_list[x] = 1
        except EOFError:
            break
    print(user_list)


main()
