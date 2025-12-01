def main():
    while True:
        try:
            x = input("input: ")
            store_x = list(x)
        except EOFError:
            break
    print(store_x)

main()
