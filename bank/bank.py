# getting input from user
greet = input("Greeting: ")

# converting lowercase and removing spaces
greet=greet.lower().strip(" ")

# checking whether the greeting consist of "hello"
if 'hello' in greet:
    print("$0")
# checking whether the greeting starting with "h"
elif greet[0] == 'h':
    print("$20")
else:
    print("$100")
