#day_02
from ast import keyword


print("hello World")
print(len("Hello world"))
input("Enter your name?")
# help("keywords")
# Variables in Python
first_name = 'nico'
last_name = 'fuentes'
country = 'United States'
city = 'Kearny'
age = 35
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'nico',
   'lastname':'fuentes',
   'natinality':'Uruguay',
   'city':'montevide'
   }
print(type(first_name), type(skills), type(person_info))
# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
first_name, last_name, country, age, is_married = 'nico', 'fuentes', 'montevideo', 250, True
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
first_name = input('What is your name: ')
age = input('How old are you? ')
print(first_name)
print(age)