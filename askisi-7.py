####
# askisi 7
#  @author Niko
#  Version  0.0.1
#  Date  18.10.2022       
#  Mathima 2     
#  
# 
# #
limit = int(input("Give me a number: "))
for i in range(0,limit+1):
    
    if (i % 3 == 0) or (i % 5 == 0): 
        print(i)
