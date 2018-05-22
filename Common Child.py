def solve(s1,s2):
    lengths = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i,x in enumerate(s1):
        for j,y in enumerate(s2):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j],lengths[i][j+1])
    return lengths[-1][-1]
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(solve(s1,s2))