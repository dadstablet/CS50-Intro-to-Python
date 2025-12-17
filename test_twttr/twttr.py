def main():
    x = input("Input: ")
    print(shorten(x))

def shorten(word):
    vowels = "AOUIEaeoui"
    short_word = []
    try:
        word = [char for char in word if char not in vowels]
        for char in word:
            short_word.append(char)
        return ''.join(short_word)
    except TypeError:
        return word

if __name__ == "__main__":
    main()
