t = int(input())
d = 0
for i in range(t):
    a,b,c = map(int, input().split())
    if(a+b+c >=2):
        d += 1
print(d)