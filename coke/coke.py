amount_prompt = print("Amount Due: 50")
change = 50

while change > 0:
    user_prompt = int(input("Insert Coin: "))
    if user_prompt == 25 or user_prompt == 10 or user_prompt == 5:
        change = change - user_prompt
        if change <= 0:
            change_due = print("Change Due: ",(change * -1))
            break
        amount_due = print("Amount Due: ",change)
    else:
        change_due = print("Amount Due: ",change)
