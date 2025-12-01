def main():
    while True:
        try:
            x = input("input: ")
        except EOFError:
            break
        store_x = list(x)
    print(store_x)

main()
