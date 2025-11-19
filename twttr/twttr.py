x = input("Input: ")
vowels = "AEOUIaeoui"

x_list = [char for vowel in x if vowel in vowels]
print(x_list)
