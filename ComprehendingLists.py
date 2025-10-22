doubles = [x * 2 for x in range(1, 11)]
tripples = [y * 3 for y in range(1, 11)]
squares = [ z * z for z in range(1, 11)]

print(doubles)
print(tripples)
print(squares)

fruits = ['apple', 'orange', 'banana']
fruits = [fruit.upper() for fruit in fruits]
fruits_characters = [fruit[2] for fruit in fruits]
print(fruits)
print(fruits_characters)

numbers = [1, -2, -3, 5, 6, -7, 8, 9, 13]
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
equal_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]

print(positive_numbers)
print(negative_numbers)
print(equal_numbers)
print(odd_numbers)

grades = [85, 42, 84, 56, 43, 11, 34]
passing_grades = [grade for grade in grades if grade > 60]

print(passing_grades)