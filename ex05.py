def fun(n,m):
    x = 1
    y = 1
    z = 1
    for i in range(n,1,-1):
        x*=i
    for i in range(m,1,-1):
        y*=i
    for i in range(n-m,1,-1):
        z*=i
    return x//(y*z)
n,m = map(int,input().split())
print(fun(n,m))