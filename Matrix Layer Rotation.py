def rotateMat(N, M, l, rot, rin, mat):
    for level in range(l):
        r = rot % len(rin[level])
        rin[level] = rin[level][r:] + rin[level][:r]
    for level in range(l):
        top = (N - 1) - 2 * level
        side = (M - 1) - 2 * level
        for i in range(top):
            mat[level][level + i] = rin[level].pop(0)  # right
        for j in range(side):
            mat[level + j][level + top] = rin[level].pop(0)  # down
        for i in range(top):
            mat[level + side][level + top - i] = rin[level].pop(0)  # left
        for j in range(side):
            mat[level + side - j][level] = rin[level].pop(0)  # up
def flatRings(M, N, mat, rot):
    l = int(min(N, M) / 2)
    rin = [[] for lay in range(l)]
    for level in range(l):
        top = (N - 1) - 2 * level
        side = (M - 1) - 2 * level
        for i in range(top):  # right
            rin[level].append(mat[level][level + i])
        for j in range(side):  # down
            rin[level].append(mat[level + j][level + top])
        for i in range(top):  # left
            rin[level].append(mat[level + side][level + top - i])
        for j in range(side):  # up
            rin[level].append(mat[level + side - j][level])
    rotateMat(N, M, l, rot, rin, mat)
M, N, rot = map(int, input().split())
mat = []
for i in range(M):
    mat.append(list(map(int, input().split())))
flatRings(M, N, mat, rot)
for row in range(M):
    for col in range(N):
        print(mat[row][col], "", end="")
    print()