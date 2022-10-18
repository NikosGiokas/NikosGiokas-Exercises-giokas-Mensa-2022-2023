####
# askisi 6
#  @author Niko
#  Version  0.0.1
#  Date  18.10.2022       
#  Mathima 2     
#  
# 
# #
num = int(input("Give me a number: "))
if (num % 3 and num % 5) == 0: 
    print("fizzBuzz")
elif (num % 5) == 0: 
    print("buzz")
elif (num % 3) == 0: 
    print ("fizz") 
else:
    print(num)