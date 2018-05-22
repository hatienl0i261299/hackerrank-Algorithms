n = int(input())
grade = []
for i in range(n):
    grade.append(int(input()))
for i in grade:
    if i < 38:
        print(i)
    elif i % 5 >= 3:
        print(i + (5-i%5))
    else:
        print(i)