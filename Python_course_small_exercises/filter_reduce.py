#filter() function
# creates a collection of elements from an iterable - list - for which a function returns True
#search results where results meet a certain criteria
import functools


friends = [("Rachel", 31),
           ("Joe", 13),
           ("Michael", 23),
           ("Joanna", 21)]

age = lambda data:data[1] >= 18

drinking_allowed = list(filter(age, friends))

for i in drinking_allowed:
    print(i)


## reduce() function
# reduce an iterable a single cumulative value
# cycling elements in an iterable until a single element remains. 

#letters = ["H", "E", "L", "L", "O"]
#word = functools.reduce(lambda x,y: x + y, letters)
#print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x,y: x * y, factorial)
print(result)