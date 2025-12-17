from twttr import twttr

def main():
    x = input("")
    shorten(x)


def shorten(word):
    assert twttr(word)  == "twttr"


if __name__ == "__main__":
    main()
