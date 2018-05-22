T = int(input())

for _ in range(T):
    n = int(input())
    a = int(input())
    b = int(input())
    a, b = sorted((a, b))
    values = sorted(set([(n - i - 1) * a + i * b for i in range(n)]))
    print(*values) 