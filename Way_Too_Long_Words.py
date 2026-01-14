p = int(input())
for _n in range(p):
    t = input()
    c = len(t)
    g = list(t)
    if c>10:
        print(g[0], end="")
        print(c-2, end="")
        print(g[-1])
    else:
        print(t)
        