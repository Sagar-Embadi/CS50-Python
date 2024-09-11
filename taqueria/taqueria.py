# addin menu dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# setting initial amount
t=0
# looping
while True:
    try:
        # get the user input
        item = input("Item: ").title()
        # checking is item in menu or not
        if item in menu:
            # adding amount of item
            t += menu[item]
            print("Total: $", end="")
            print("{:.2f}".format(t))
    except (KeyError, EOFError):
        # printing new line and break the loop
        print()
        break

