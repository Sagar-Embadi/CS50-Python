# creating empty dictionary
grocery = {}
# loop forever
while True:
    try:
        # get input from user
        item = input("").upper()
        # checking whether the item is in grocery or not
        if item in grocery:
            # if it presented then add count of item
            grocery[item] += 1
        else:
            # else adding item to list
            grocery[item] = 1
    except EOFError:
        # loop for items in grocery
        for key in sorted(grocery.keys()):
            # printing items count and name to output
            print(grocery[key], key)
        break # breaking the loop
