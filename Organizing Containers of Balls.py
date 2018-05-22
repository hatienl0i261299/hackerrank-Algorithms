for _ in range(int(input())):
    m = []
    n = int(input())
    for i in range(n):
        m_t = [int(temp) for temp in input().strip().split(' ')]
        m.append(m_t)
    sv = []
    sh = []
    for i in range(n):
        sv.append(0)
        sh.append(sum(m[i]))
        for j in range(n):
            sv[i] += m[j][i]
    sv.sort()
    sh.sort()
    if sv == sh:
        print("Possible")
    else:
        print("Impossible")