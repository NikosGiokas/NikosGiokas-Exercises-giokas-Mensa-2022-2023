
num1 = input("Give me a number: ")
num2=input("give me another number: ")
num3=input("give me another number: ")
if num1 > num2 and num3:
    print(str(num1)+" is bigger")
if num2 > num1 and num3:
    print(str(num2)+" is bigger")
if num3 > num2 and num1:
    print(str(num3)+" is bigger")
if num3 == num2 and num1 == num2:
    print("they are equal")