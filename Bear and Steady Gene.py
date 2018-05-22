from collections import Counter
import sys

n = int(input())  # length of string
s1 = input()
s = Counter(s1)
le = int(n / 4)  # ideal length of each element
comp = {'A': le, 'G': le, 'C': le, 'T': le}  # dictionary containing equal number of all elements
s.subtract(comp)  # Finding by how much each element ('A','G'...) is in excess or loss
a = []
b = []
for x in s.values():  # storing frequency(s.values--[4,2]) of elements which are in excess
    if (x > 0):
        a.append(x)
for x in s.keys():  # storing corresponding elements(s.keys--['A','G'])
    if (s[x] > 0):
        b.append(x)
mnum = sum(a)  # minimum substring length to start with
if (mnum == 0):
    print(0)
    sys.exit()
flag = 0
while (mnum <= n):  # (when length 4 substring with all the A's and G's is not found increasing to 5 and so on)
    for i in range(n - mnum + 1):  # Finding substrings with length mnum in s1
        for j in range(len(a)):  # Checking if all of excess elements are present
            if (s1[i:i + mnum].count(b[j]) == a[j]):
                flag = 1
            else:
                flag = 0

        if (flag == 1):
            print(mnum)
            sys.exit()
    mnum += 1