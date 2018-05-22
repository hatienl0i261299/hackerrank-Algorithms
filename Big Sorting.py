n = int(input())
unsorted = []
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)

unsorted.sort(key=int)
print('\n'.join(str(e)for e in  unsorted))