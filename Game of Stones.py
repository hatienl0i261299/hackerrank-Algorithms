if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        if n > 5:
            D = [1] * (n + 1)
            D[1] = 2
            D[2] = 1
            D[3] = 1
            D[4] = 1
            D[5] = 1
            for j in range(n+1):
                if D[j - 2] == 2 or D[j - 3] == 2 or D[j - 5] == 2:
                    D[j] = 1
                else:
                    D[j] = 2
            if D[n] == 1:
                print("First")
            else:
                print("Second")
        else:
            if n == 1:
                print('Second')
            else:
                print('First')