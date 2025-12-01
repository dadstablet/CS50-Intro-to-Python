def main():
    user_list = {}
    while True:
        try:
            value_count = 1
            x = input()
            if x in user_list:
                value_count += 1
            user_list[x] = value_count
        except EOFError:
            break
    return output(user_list)

def output(dict):
    for key in sorted(dict):
        print(dict[key], key.upper())

main()
