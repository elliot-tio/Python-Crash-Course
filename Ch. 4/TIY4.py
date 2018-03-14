# 4-3 Counting to twenty
print("4-3. Counting to twenty", end='\n')
for value in range(1,21):
    print(value, end='\n')

# 4-4 One Million
print("4-4. List of the numbers from one to one million", end='\n')
million = list(range(1, 100001))
for number in million:
    print(number, end='\n')

# 4-5. Summing a million
print("4-5. Summing a million")
print("Min: " + str(min(million)))
print("Max: " + str(max(million)))
print("Sum: " + str(sum(million)))

# 4-6. Odd Numbers
print("4-6. Odd Numbers")
odd_list = list(range(1, 21, 2))
for odds in odd_list:
    print(odds)

# 4-7. Threes
print("4-7. Threes")
threes = list(range(3, 31, 3))
for three in threes:
    print(three)

# 4-8. Cubes
print("4-8. Cubes")
cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension
print("4-9. See 4-8.")

# 4-10. Slices
print("4-10. Slices")
print("The first three items in the list are: " + str(threes[:3]))

# 4-13. Buffet
print("4-13. Buffet tuples")
print("Original menu:\n")
buffet = ("steak", "fried rice", "french fries", "eggs", "juice")
for food in buffet:
    print(food)
new_buffet = ("steak", "fried chicken", "octopus", "eggs", "juice")
print("\nNew menu:\n")
for food in new_buffet:
    print(food)
