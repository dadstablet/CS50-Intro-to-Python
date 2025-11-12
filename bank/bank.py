x = input("Greeting: ")

clean_x = x.strip().lower()

if clean_x.startswith("hello"): print("$0")
else:
    if clean_x.startswith("h"): print ("$20")
    else: print("$100")
