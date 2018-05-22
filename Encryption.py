import math
s = input().strip()
a = math.floor(math.sqrt(len(s)))
b = math.ceil(math.sqrt(len(s)))
if (a*b) < len(s):
    a = b
for i in range(b):
    print(s[i:len(s):b],end=' ')