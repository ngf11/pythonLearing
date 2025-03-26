'''
#Strings

print("Hello")
print("What's Your name")

frist_name = "nico"
food ="Burger"
email = "nico123@caca.com"

print(f"My name is {frist_name}")
print(f"I like {food}")

#intigers
age = 36 
quantity = 3 
price = 5 
print(f"You are {age} years old")
print(f"Hi {frist_name} you are buying {quantity} {food}s. The price for each is ${price} the total is {quantity * price}")


#Float
pi = 3.14 

#boolean 
is_student = True
is_american = True
lights_are_on = False

if is_american:
    print("Welcome Home")
else:
    print("Welcome to your new home")

Typecasting is the process of converting a variable from one data type to another str() int() float() bool(). This is usefull when handeling user input

name = "nico"
age = 36
gpa = 3.6
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)
print(type(gpa))
##3
##<class 'int'>

age = float(age)
print(age)
print(type(age))
##36.0
##<class 'float'>

age = str(age)
print(age)
print(type(age))
##36.0
##<class 'str'>

name = bool(name)
print(name)
print(type(name))

##input() a function that prompts user for input. Returns user data as a string

name = input("What is your name?")
age = int(input("How old are you?"))
print(f"Hi {name}")
age = age + 1
print(f"Happy Bday {name} You are {age}")
## Area of a rectangle

length = int(input("What is the length of the rectangle?"))
width = int(input("What is the width of the rectangle?"))
area_rec = length * width
print(f"The length is: {length} The width is: {width} The area of the Rectangle: {area_rec}")
## Shoping cart

item = input ("What would you like to buy?")
price = float(input("What is the price of the item?"))
quantity = int(input("How many would you like? "))
total = price * quantity

##Madlibs Game
adjective = input()
noun = input()
print(f"Today I went to a {adjective} Zoo.")
print(f"In an exhibit I saw {noun}")


## Math
friends = 0

# friends = friends + 1
friends += 5

# friends = friends - 2

friends -= 2

friends *= 3

friends /= 3

## remainder %

friends %= 2



friends **= 2

print(f"You have {friends} friends")

## built in functions MATH


x = 3.14

y = -4

z = 5

# result = round(x) round number
# result = abs(y) absolut 
# result = pow(z, 2) pow(base, power)
# result = max(x,y,z) maximum value
result = min(x,y,z)

print(result)
## Import Math
 
import math

x = 9
y = 9.5
z = 9.5
#If you need pi
print(math.pi)
print(math.e)
# square root of a number
result = math.sqrt(x)
print(result)
roundUp = math.ceil(y)
print(roundUp)

#round down floor
round_down = math.floor(z)

print(round_down)

#ceil rounds a floating point up
# circumference of a circle

import math
pi = math.pi
radius = float(input("What is the radius of the ciercle? :"))

circumference = math.floor( 2 * (pi * radius))

print(f"The circumference of the cirtcle is {circumference}")

area = pi * pow(radius, 2)

print(f"The area is {round(area, 2)}")
import math
a = float(input("enter side a:"))
b = float(input("enter side b:"))

hype =math.sqrt(pow(a,2) + pow(b, 2))

print(f"the Hype  is {hype}")
'''
