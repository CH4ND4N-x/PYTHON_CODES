
#Area and Perimeter of Circle
import math
x = input("Enter the radius of circle:") #taking radius input

area=(math.pi*math.pow(int(x), 2)) #finding area

per=2*math.pi*int(x) #findind perimeter

#printing area and perimerter
print("Area:"+str(area))

print("Perimeter:"+str(per))