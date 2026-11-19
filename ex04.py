def fun3(n):
    x = 1
    for i in range(n,1,-1):
        x*=i
    return x
y = fun3(9)
print(y)