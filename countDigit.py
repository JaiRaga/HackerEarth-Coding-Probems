if __name__ == "__main__":
    s = map(str, input().strip())
    s = [int(i) for i in s]
    for i in range(10):
        print(i, s.count(i))
