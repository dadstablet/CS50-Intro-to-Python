def convert(x):
    step_1 = x.replace(":)","🙂")
    step_2 = step_1.replace(":(","🙁")
    print(step_2)

def main():
    text = input()
    conv_text = convert(text)
    print(text)

main()
