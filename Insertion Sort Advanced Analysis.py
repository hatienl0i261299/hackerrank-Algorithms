class BinaryIndexedTree():
    def __init__(self, sz):
        self.sz = sz
        self.tree = [0] * sz
    def update(self, idx, val):
        while (idx <= self.sz):
            self.tree[idx] += val
            idx += (idx & -idx)
    def read(self, idx):
        sum = 0
        while (idx > 0):
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum
if __name__ == '__main__':
    t = input()
    for _ in range(int(t)):
        n = input()
        arr = list(map(int, input().split()))
        cnt = 0
        bit = BinaryIndexedTree(10 ** 7 + 1)
        for val in reversed(arr):
            bit.update(val, 1)
            cnt += bit.read(val - 1)
        print(cnt)