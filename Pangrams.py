def solve(s):
    return len(set(c.lower() for c in s if c != ' '))
if __name__ == '__main__':
    s = input()
    if solve(s) == 26:
        print("pangram")
    else:
        print('not pangram')