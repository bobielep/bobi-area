# check point one
# calculator.py 
import math


print("==================")
print("Area Calculator 📐")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

choose = int(input("Which shape:"))

if choose == 1:
    hight = int(input("height:"))
    base = int (input("base:"))
elif choose == 2:
    length = int(input("length:"))
    width = int(input("width:"))
elif choose == 3:
    side = int(input("side:"))
elif choose == 4:
    radius = int(input("radius:"))
else:
    print("Quit")

if choose == 1:
    area = (hight*base)/2
    print("The area is" , area)
elif choose == 2:
    area = length*width
    print("The area is" , area)
elif choose == 3:
    area = side**2
    print("The area is" , area)
elif choose == 4:
    area = math.pi*(radius**2)
    print("The area is" , area)
else:
    print("Quit")
