####
# Mathima 4
# askisi 1
# 
#  @author Niko
#  Version  0.0.1
#  Date  5.11.2022    
#    
# #

def nameFunc():
    print("Niko")


for i in range(11):
    nameFunc()
print("___________________\n")

####
# Mathima 4
# askisi 2
# 
#  @author Niko
#  Version  0.0.1
#  Date  5.11.2022    
#    
# #
def nameInput():
    name = input("what is your name?\n ")
    return name

print("hi",nameInput())
print("___________________\n")


####
# Mathima 4
# askisi 3
# 
#  @author Niko
#  Version  0.0.1
#  Date  5.11.2022    
#    
# #
def multipleName3Times():
    for i in range(3):
        nameFunc()
def multiplyNameTimes2():
    for i in range(2):
        multipleName3Times()
multiplyNameTimes2()
print("___________________\n")

####
# Mathima 4
# askisi 4
# 
#  @author Niko
#  Version  0.0.1
#  Date  5.11.2022    
#    
# #
n = int(input("Poses fores theleis na emfanistei to onoma? "))
for i in range(n):
        nameFunc()

print("___________________\n")