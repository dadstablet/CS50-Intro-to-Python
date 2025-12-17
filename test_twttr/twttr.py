def main():
    x = input("Input: ")
    print(twttr(x))

def twttr(word):
    vowels = "AEOUIaeoui"
    word = [char for char in word if char not in vowels]
    short_word = []
    for char in word:
        short_word.append(char)
    return ''.join(short_word)

if __name__ == "__main__":
    main()
