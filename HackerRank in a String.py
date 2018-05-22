def solve(s):
    h = "hackerrank"
    if len(s) < len(h):
        return "NO"
    j = 0
    for i in range(len(s)):
        if j < len(h) and s[i] == h[j]:
            j += 1
    if j == len(h):
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        print(solve(s))