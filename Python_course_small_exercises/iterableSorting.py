# sort() method or sort() function

students = ["John", "Margaret", "Charles", "Anne", "Kirby"]

students.sort(reverse=True)

for i in students:
    print(i)


students = ("John", "Margaret", "Charles", "Anne", "Kirby")

sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)


students = [("John", "A", 20),
            ("Margaret", "B", 34),
            ("Charles", "F", 23),
            ("Anne", "D", 45),
            ("Kirby", "A", 28)]

age = lambda ages:ages[2]
students.sort(key=age)

for i in students:
    print(i)


students = (("John", "A", 20),
            ("Margaret", "B", 34),
            ("Charles", "F", 23),
            ("Anne", "D", 45),
            ("Kirby", "A", 28))

grade = lambda grades:grades[1]
sorted_students2 = sorted(students, key=grade)

for i in sorted_students2:
    print(i)
