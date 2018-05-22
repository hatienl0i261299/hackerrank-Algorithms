n = int(input())
matrix = []
a = []
b = []
step1 = 0
step2 = -1
for i in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(len(matrix)):
    a.append(matrix[i][step1])
    step1 += 1
    b.append(matrix[i][step2])
    step2 -= 1
print(abs(sum(a) - sum(b)))