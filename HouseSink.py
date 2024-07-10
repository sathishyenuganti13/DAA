import math

def calcRadius(Area):
    return math.sqrt((Area*2)/math.pi)
    
def calcDistance(x,y):
    return math.sqrt(x**2+y**2)
    
x = int(input("Enter x co-ordinate  : "))
y = int(input("Enter y co-ordinate  : "))

dis = calcDistance(x,y)

l=50

while(dis >= calcRadius(l) ):
    l+=50

print("No.of years until house to sink : ",l//50)
    
    

