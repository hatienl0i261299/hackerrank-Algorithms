n = int(input())
scores = list(map(int,input().split()))
scores = list(set(scores))
scores.sort()
m = int(input())
alice_scores = list(map(int,input().split()))
count = 0
x = len(scores)
for a in alice_scores:
    while count < x and a >= scores[count]:
        count += 1
    print(x + 1 - count)