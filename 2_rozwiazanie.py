# Zadanie 1
first_name = 'James'
last_name = 'Michaels'
email = 'jmichaels@example.com'
phone = '12343214433'
age = 44

print(
    f"My name is {first_name} {last_name}.\nI'm {age} years old.\nYou can contact me via email: {email} or phone: {phone}.")

# Zadanie 2
pi = 3.1415
r = 2
circumference = 2 * pi * r
area = pi * r ** 2

# Zadanie 3
a = 5
b = 13
c = (a ** 2 + b ** 2) ** 0.5
print(round(c, 2))
triange_circumference = a + b + c
triange_area = a * b / 2
print(triange_circumference)
print(triange_area)

# Zadanie 4
"""
1. Wszystkie osoby powyżej 65 roku życia
2. Kobiety do 16 roku życia włącznie lub powyżej 45 roku życia 
3. Mężczyźni od 20 do 40 roku życia włącznie
"""
sex = 'f'
age = 16

condition1 = age > 65
condition2 = sex == 'f' and (age <= 16 or age >= 45)
condition3 = sex == 'm' and (age <= 20 or age >= 40)
can_use_promotion = condition1 or condition2 or condition3
print(f'Sex: {sex}, age: {age}, can use promotion: {can_use_promotion}')
