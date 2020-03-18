if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    x = str(x)
    x = [i for i in x]
    y = [i for i in x]
    val = 0

    if k == 0:
        y = "".join(y)
        y = int(y)
        print(y)
    else:
        for i in range(len(x)):
            if x[i] != '9':
                y[i] = '9'
                val += 1
            if val == k:
                break
        y = "".join(y)
        y = int(y)
        print(y)
