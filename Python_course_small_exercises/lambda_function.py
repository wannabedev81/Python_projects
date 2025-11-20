# lambda functions are written in 1 line with lambda keyword. 
# accepts any number of arguments but only one expression
# useful for short usage 

# lambda parameters : expression

# example code
# def double(x):
#   return x * 2
# print (double(5))

double = lambda x:x * 2

print(double(2))

multiply = lambda x,y:x * y
print(multiply(5, 6))

add3 = lambda x,y,z: x + y + z
print(add3(5,4,6))

fullname = lambda firstname, lastname: firstname + " " + lastname
print(fullname("John", "Wick"))

age_check = lambda age: True if age > 18 else False
print(age_check(12))
print(age_check(8))
print(age_check(23))