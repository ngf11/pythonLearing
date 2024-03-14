from cmath import inf, pi
from xml.etree.ElementTree import PI


first_name = 'nico'
last_name  = 'fuentes'
fullname = first_name + " " + last_name
country = "Uruguay"
city = "Montevide"
age =35
year = 1989
is_married = False
didi , milo , baby, dog = 'Didi Wu TinTin', 'Fat Man', 'dylan', 'momo'
print(type(first_name))
print(type(last_name))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(didi))
print(type(milo))
print(type(baby))
print(type(dog))
print(len(first_name))
print(len(last_name))
print(len(first_name) ==  len(last_name)) 
num_one = 5
num_two = 4
print(num_one + num_two)
print(num_one - num_two)
print(num_one * num_two)
print(num_one / num_two)
print(num_one % num_two)
print(num_one // num_two)
print(num_one ** num_two)
radius = 30
pi = 3.14
area_of_circle = pi * radius * radius
circum_of_circle = 2 * pi * radius
print(circum_of_circle)
print(area_of_circle)
user_input = input("enter radius")
# print(type(user_input))
print(pi * int(user_input) * int(user_input))
info = {
    'fistName': input('What is your name?'),
    'lastName' : input('what is your last name?'),
    'age': input('How old are you?'),
    'city':  input("What is your city?")
}
print(info)