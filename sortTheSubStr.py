if __name__ == "__main__":
    T = int(input().strip())
    for i in range(T):
        s, n, m = map(str, input().strip().split())

        n = int(n)
        m = int(m)

        if n == 0 and m >= len(s):
            s = [i for i in s]
            s = s.sort(reverse=True)
            # print('11111111111111111111111111111')
        else:
            cut = s[n:m+1]
            cut = [i for i in cut]
            cut.sort(reverse=True)
            nS = ''
            ncut = ''

            for i in cut:
                ncut += i
            if m == len(s) - 1:
                s = s[:n] + ncut
            else:
                s = s[:n] + ncut + s[m+1:]
            # print('2222222222222222222222222222222')
        print(s)
