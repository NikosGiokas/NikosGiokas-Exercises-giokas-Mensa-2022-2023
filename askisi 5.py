####
# askisi 5
#  @author Niko
#  Version  0.0.1
#  Date  15.10.2022       
#  Mathima 2     
#  
# 
# #


limit = int(input("Give me a number: "))

for i in range(0,limit+1):
    
    if (i % 2) == 0: 
        print (str(i)+" even") 
    else: 
        print(str(i) +" odd")