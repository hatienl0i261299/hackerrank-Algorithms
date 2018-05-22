def insertion_sort(l):
    l2 = l.sort(key=int)
    return l2
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))