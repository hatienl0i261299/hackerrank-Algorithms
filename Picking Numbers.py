'''
length = int(input())
arr = list(map(int,input().split()))
counts = {}
sortedCounts = []
answer = 0
for num in arr:
    counts[num] = counts.get(num,0) + 1
for k,v in sorted(counts.items()):
    sortedCounts.append([k,v])
for i in range(len(sortedCounts) - 1):
    if sortedCounts[i+1][0] - sortedCounts[i][0] < 2:
        totalCount = sortedCounts[i][1] + sortedCounts[i+1][1]
        answer = totalCount if totalCount > answer else answer
print(answer)
'''
n = int(input())
a = list(map(int,input().split()))
maximum = 0
diff = 1
for k in a:
    n1 = a.count(k)
    n2 = a.count(k-diff)
    maximum = max(maximum,n1+n2)
print(maximum)