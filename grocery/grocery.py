def main():
    user_list = []
    while True:
        try:
            x = input("input: ")
            user_list.append(x)
        except EOFError:
            break
    print(user_list)

def grocery(list_x):
    for x in list_x:
        

main()
