x = input("Greeting: ")

clean_x = x.strip().lower()

if clean_x.startswith("hello") == "TRUE": print("$0")
# elif clean_x.startswith("hello") == FALSE AND clean_x.startswith("h") == TRUE: print ("$20")
else: print("$100")
