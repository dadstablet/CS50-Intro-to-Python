amount_prompt = print("Amount Due: 50")

while True:
    user_prompt = int(input("Insert Coin: "))
    change = change - user_prompt
    change_due = print("Change due: ",change)
    # if user_prompt != 50 or user_prompt != 25 or user_prompt != 10 or user_prompt != 5:
    #     break
