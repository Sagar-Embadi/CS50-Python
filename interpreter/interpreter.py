# get input from user
x,y,z = input("Expression: ").split(" ")
# convertin x , z into float
x,z = float(x),float(z)
# solving expressions
if y=="+" :
    print(x+z)
elif y=="-" :
    print(x-z)
elif y == "*" :
    print(x*z)
elif y == "/" :
    print(x/z)
