grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Решение 1
D = {}
L = list(sorted(students))
for i in range(len(students)):
 D[L[i]] = sum(grades[i])/len(grades[i])
print(D)

# Решение 2
print(D:={student: sum(g)/len(g) for student, g in zip(sorted(students), grades)})