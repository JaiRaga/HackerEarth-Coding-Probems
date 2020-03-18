if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        l, w = map(int, input().strip().split())
        print(max(l // w, w // l))
