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
    area = (hight*base)/2
    print("The area is" , area)
elif choose == 2:
    length = int(input("length:"))
    width = int(input("width:"))
    area = length*width
    print("The area is" , area)
elif choose == 3:
    side = int(input("side:"))
    area = side**2
    print("The area is" , area)
elif choose == 4:
    radius = int(input("radius:"))
    area = math.pi*(radius**2)
    print("The area is" , area)
else:
    print("Quit")

# uhhhh  I made some upgrades ，Now it looks even better.
