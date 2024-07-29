students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_aver = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
               sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
               sum(grades[4])/len(grades[4])]
students_final = sorted(students)
a = {'a': 5, 'b': 6}     #обьединить в словарь
dict1 = dict(zip(students_final, grades_aver))
print(dict1)