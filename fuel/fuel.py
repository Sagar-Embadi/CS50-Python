# looping using while operator
while True:
    # get the user input
    fuel = input("Fraction: ")
    # trying methods
    try:
        x,y = fuel.split("/")
        x=int(x)
        y=int(y)
        f=x/y
        if f <= 1:
            break
    # excepting the errors
    except(ValueError, ZeroDivisionError):
        pass
p = round(f*100)
# checking whether fuel is empty
if p<= 1 :
    print("E")
# checking whether fuel is full
elif p>=99 :
    print("F")
# else print fuel in percentage
else:
    print(f"{p}%")
