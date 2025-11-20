##creating a new list with less syntax
## mimic certain lambda function

#squares = []
#for i in range(1, 11):
#    squares.append(i*i)
#print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 0]

passed_students = list(filter(lambda x: x>60, students))
print(passed_students)

#with list comprehension

#passed_students = [i for i in students if i >= 60]

#if we need an else statement
passed_students = [ i if i >= 60 else "FAILED" for i in students]
print(passed_students)