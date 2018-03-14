# 5-1. Conditional Tests
print("5-1. Conditional Tests")
car = 'audi'
print("Is car == 'audi'? I predict true")
print(car == 'audi')
print("\nIs car == 'subaru'? I predict false")
print(car == 'subaru')

# 5-2. More Conditional Tests
print("\n5-2. More Conditional Tests")
drink = 'cola'
print("Is drink == 'Cola'? I predict false")
print(drink == 'Cola')
print("\nIs drink == 'cola'? I predict true")
print(drink == 'cola')
food = 'Pizza'
print("\nIs food == 'pizza'? I predict true")
print(food.lower() == 'pizza')

# 5-3 Alien Colors
print("\n5-3. Alien Colors #1")
alien_color = 'red'
if alien_color == 'green':
    print("You have earned 5 points!")
if alien_color == 'red':
    print("The alien is red")

# 5-4. Alien Colors 2
print("\n5-4. Alien Colors #2")
alien_color = 'yellow'
if alien_color == 'green':
    print("You have earned 5 points!")
else:
    print("You have earned 10 points!")

# 5-5. Alien Colors 3
print("\n5-5. Alien Colors #3")
points = 0
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("You have earned " + str(points) + " points!")

alien_color = 'green'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("You have earned " + str(points) + " points!")

alien_color = 'red'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print("You have earned " + str(points) + " points!")

# 5-6. Stages of life
print("\n5-6. Stages of Life")
age = 66
stage = ''
if age < 2:
    stage = 'baby'
elif age >= 2 and age < 4:
    stage = 'todler'
elif age >= 4 and age < 13:
    stage = 'kid'
elif age >= 13 and age < 20:
    stage = 'teenager'
elif age >= 20 and age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'

print("Your age is " + str(age) + " and your stage of life is " + stage + ".")

# 5-7. Favourite Fruit
print("\n5-7. Favourite fruits")
fruits = ['bananas', 'apples', 'oranges']

if 'bananas' in fruits:
    print("I like bananas")
if 'oranges' in fruits:
    print("I like oranges")
if 'mangoes' in fruits:
    print("I like mangoes")
if 'pineapples' in fruits:
    print("I like pineapples")
if 'apples' in fruits:
    print("I like apples")
