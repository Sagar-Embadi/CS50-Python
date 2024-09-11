# importing inflect module
import inflect
p = inflect.engine()
# create the empty list
names = []
# loop forever until break
while True :
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError :
        print()
        break
# print the output
print("Adieu, adieu, to",p.join(names))
