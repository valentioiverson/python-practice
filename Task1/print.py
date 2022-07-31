if __name__ == '__main__':
    n = int(input())
    i = 1
    a = 0
    for i in range(n + 1):
        if i < 10:
            a = 10 * a + i
        elif i < 100:
            a = 100 * a + i
        elif i < 1000:
            a = 1000 * a + i
    print(a)
