numbers = list(map(int,input().split()))
x = sum(numbers)
print(x - max(numbers), x - min(numbers))