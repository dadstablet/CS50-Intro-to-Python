def main():
    user_list = {}
    value_count = 1
    while True:
        try:
            x = input("input: ")
            user_list[x] = value_count
            if x in user_list:
                value_count += 1
        except EOFError:
            break
    print(user_list)


main()
