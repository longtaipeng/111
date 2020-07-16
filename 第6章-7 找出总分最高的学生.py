n = int(input())
student = {}
for i in range(n):
    a, b, c, d, e = input().split(' ')
    list1 = [int(c), int(d), int(e)]
    student[b] = [a]
    student[b].append(list1)
student2 = {}
for key, value in student.items():
    student2[key] = value[1]
student3 = max(student2, key=student2.get)
print(student3, student[student3][0], sum(student[student3][1]))
