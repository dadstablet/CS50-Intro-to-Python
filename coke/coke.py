amount_prompt = print("Amount Due: 50")
change = 50

while change >=0:
    user_prompt = int(input("Insert Coin: "))
    if user_prompt == 50 or user_prompt == 25 or user_prompt == 10 or user_prompt == 5:
        change = change - user_prompt
        change_due = print("Change due: ",change)
    else:
        change_due = print("Change due: ",change)

