def solve(w):
    i = len(w) - 1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(w) - 1
    while w[j] <= w[i-1]:
        j -= 1
    w[i-1],w[j] = w[j],w[i-1]
    w[i:] = w[len(w) - 1:i-1:-1]
    return True
if __name__ == '__main__':
    for _ in range(int(input())):
        w = list(input())
        if solve(w):
            print(''.join(w))
        else:
            print("no answer")

