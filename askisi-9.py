####
# askisi 8
#  @author Niko
#  Version  0.0.1
#  Date  18.10.2022       
#  Mathima 2     
#  
# 
# #
limit = int(input("Give me a limit: "))

for num in range(1, limit+1):
    isPrime = True
    for j in range(2, int(num/2)+1):
        if (num % j) == 0:
            isPrime = False
            break
    if isPrime:
        print(num, " is a prime number")
