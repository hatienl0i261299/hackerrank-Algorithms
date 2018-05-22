def isPalindrome(s):
    for idx in range(len(s)//2):
        if s[idx] != s[len(s) - idx -1]:
            return False
    return True
def solve(s):
    for i in range((len(s) + 1)//2):
        if s[i] != s[len(s)- i - 1]:
            if isPalindrome(s[:i] + s[i+1:]):
                return i
            else:
                return len(s) - i - 1
    return -1
if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        print(solve(s))