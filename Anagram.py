def solve(s):
    if len(s) % 2 ==1:
        return -1
    else:
        x = len(s) // 2
        count = 0
        lst = []
        lst.extend(s)
        s1 = lst[:x]
        s2 = lst[x:]
        for i in range(len(s1)):
            if s2.count(s1[i]) != 0:
                s2.remove(s1[i])
            else:
                count += 1
        return count
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input().strip()
        print(solve(s))