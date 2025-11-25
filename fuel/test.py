input = input("Put input here ")

split = input.split("/")
numer = int(split[0])
denom = int(split[1])
percent = int(round((numer/denom)*100))

print(percent)
