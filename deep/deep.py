x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

clean_x = str(x).strip().lower()
if clean_x == "42": print("Yes")
elif clean_x == "forty-two": print("Yes")
elif clean_x == "forty two": print("Yes")
else: print("No")
