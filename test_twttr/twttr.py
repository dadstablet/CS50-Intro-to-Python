def main():
    x = input("Input: ")
    print(shorten(x))

def shorten(word):
    vowels = "AOUIEaeoui"
    try:
        word = [char for char in word if char not in vowels]
        short_word = []
        for char in word:
            short_word.append(char)
        return ''.join(short_word)
    except TypeError:
        return "Error"

if __name__ == "__main__":
    main()
