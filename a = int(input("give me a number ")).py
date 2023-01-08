try:
    a = int(input("give me a number: "))
    b = int(input("give me a number: "))
except ValueError:
    print("error")
    exit()
c = a/b
try:
    c=a/b
except ZeroDivisionError:
    print("cannot divide by zero")
    exit

print(a,"/",b,"=",c)



