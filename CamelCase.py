if __name__ == '__main__':
    s = input().strip()
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    print(count)