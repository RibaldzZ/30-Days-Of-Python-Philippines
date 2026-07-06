
# Variables en Python

first_name = 'Mark'
last_name = 'Ribaldz'
country = 'Philippines'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Mark', 
    'lastname':'Ribaldz', 
    'country':'Philippines',
    'city':'Helsinki'
    }

# Imprimir los valores almacenados en las variables

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

# Declarar múltiples variables en una línea

first_name, last_name, country, age, is_married = 'Mark', 'Ribaldz', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)