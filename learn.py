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

## IF statments do some code IF a condion is TURE
# Else do something ElSE
#  

age = int(input("What is your age?: "))
if age >= 100:
    print("How are you still here!")
elif age >= 18:
    print("You are now and adult")
elif age < 0:
    print("Wher you born yet")
else: 
    print("You are still a Kid")
response = input("Would you like food?: (Y/N)")

if response == "Y":
    print("Okay good")
else:
    print("No food for you")
name = input("What is your name?: ")

if name == "":
    print("You didn't enter your name")
else:
    print(f"Hello, {name}")
for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("Not for sale")
#calculator 

operator = input("Choose an operator? (add = + | sub = - | muiltipcation = * | devision = / : ")
num1 = float(input("write your frist number: "))
num2 = float(input("write your second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Total is: {round(result, 3)}")
elif operator == "-":
     result = num1 - num2
     print(f"Total is: {round(result, 3)}")
elif operator == "*":
     result = num1 * num2
     print(f"Total is: {round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"Total is: {round(result, 3)}")
else:
    print(f"{operator} is not valid")
    
weight = float(input("Enter your weight?: "))
unit = input("Kgs or Lbs: ")

if unit == "Kgs":
    result = print(f"Your weight in lbs is {round(weight * 2.20462, 2 )}")
elif unit == "Lbs":
    result = print(f"Your weight in Kgs is {round(weight / 2.20462, 2 )}")
else:
    print("Your enter the wrong info")
# Logical Operators: it evaluates multiple operations(or, AND, NOT)
#           or = If one of the conditions is met
#           and = If both Contions is met
#           not =  it inverts the condiont (Not false = True, Not true = False)


#conditional expressions: Are a one line short cut for the if-else statments(terany operators)
#                   Print or assing one value based on the condition 
#               return X if conditon is true else Y

#positive
num = 5 

print("Good" if num > 0 else "notgood")
#even or odd
num = 7
a =6
b =7
print( "Even" if num % 2 == 0 else "odd"   )
1:27
'''
