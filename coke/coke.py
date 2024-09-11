# setting due amount
amount_due = 50
# creating loop
while amount_due > 0:
    # print amount due
    print("Amount Due:", amount_due)
    # getting user input for insert coin
    coin = int(input("Insert Coin:"))
    # checking insert coin
    if coin in [5, 10, 25]:
        amount_due-=coin
# print the change owed
change = abs(amount_due)
print("Change Owed:", change)
