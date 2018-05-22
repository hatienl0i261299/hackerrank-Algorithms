
def can_convert(s,t,k):
    if len(s) + len(t) <= k:
        return True
    c = size_diff(s,t)
    x = k - (len(s) - c) - (len(t) - c)
    if x >= 0 and x % 2 == 0:
        return True
    return False

def size_diff(s,t):
    m = min(len(s),len(t))
    if m == 0:
        return 0
    for i in range(min(len(s),len(t))):
        if s[i] != t[i]:
            return i
    return m
if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input())
    if can_convert(s,t,k) == True:
        print("Yes")
    elif can_convert(s,t,k) == False:
        print("No")