t = int(input())
for _ in range(t):
    s = input()
    s_len = len(s)
    funny = True
    for i in range(1, int(s_len / 2) + 1):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[s_len - i - 1]) - ord(s[s_len - i])):
            print('Not Funny')
            break
    else:
        print('Funny')