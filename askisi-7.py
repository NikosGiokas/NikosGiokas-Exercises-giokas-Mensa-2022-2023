####
# askisi 8
#  @author Niko
#  Version  0.0.1
#  Date  18.10.2022       
#  Mathima 2     
#  
# 
# #

#i askisi 7 einai alli kai tin exeis kanei lathos 
limit = int(input("Give me a number: "))
asteraki = "*"
for i in range(0,limit+1):
    asteraki = asteraki + "****"
    
    print(asteraki)
    
for i in range(0,limit+1):
    asteraki = asteraki[:-4]
    
    print(asteraki)
    
