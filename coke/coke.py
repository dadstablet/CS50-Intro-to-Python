amount = 50
amount_prompt = print("Amount Due: ",amount)
user_prompt = int(input("Insert Coin: "))

if user_prompt == 50 or user_prompt == 25 or user_prompt == 10 or user_prompt == 5:
    print(user_prompt)
else:
    amount_prompt
# while amount >= 0:
#     amount = amount - user_prompt
#     user_prompt
