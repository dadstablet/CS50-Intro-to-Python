import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        link = re.search(r"<iframe src=\"(?:https?://)?(?:www\.)?(youtube)\.com/embed/(.*)\"></iframe>",s)
        youtube, id = link.group(1), link.group(2)
        youtube = re.sub(r"youtube", "youtu.be", youtube)
        short = f"https://{youtube}/{id}"
        return short
    except AttributeError:
        return None

# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe> into ---> https://youtu.be/xvFZjo5PgG0


if __name__ == "__main__":
    main()
