# getting input from user
camelCase= input("camelCase: ")

#printing snake_case
print("snake_case: ", )

#loop throughout the letters
for letter in camelCase:

    # checking if the letter is in uppercase
    if letter.isupper():

        # printing underscore and lowercaseing the letter
        print("_"+letter.lower(), )
    else:
        # otherwise, print the letter
        print(letter, )

# print the space(new line)
print()
