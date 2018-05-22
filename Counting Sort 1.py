__ = input()
sol = [0] * 100
for i in [int(n) for n in input().split()]:
    sol[i] += 1
print(*sol)