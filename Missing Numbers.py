itt = int(input())
A = map(int,input().split())
itt_b = int(input())
B = map(int,input().split())
mini = min(B)
answer = []
lis = [0 for x in range(102)]
for k in A:
    lis[k-mini] -= 1
for d in B:
    lis[d-mini] += 1
for ind, ele in enumerate(lis):
    if ele != 0:
        answer.append(ind+mini)
print(' '.join(map(str,answer)))