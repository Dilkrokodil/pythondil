students = {}
a = 0
Kolvo_stud = int(input("Количество студентов: "))
for i in range(1, Kolvo_stud + 1):
    stud = input(str(i) + "-й студент: ")
    ball = int(input("Балл: "))
    students[stud] = ball
    a += ball
sredball = a/Kolvo_stud
print(sredball)
for i in students:
    if students[i] > sredball:
        print("Студенты с баллом выше среднего:", i)