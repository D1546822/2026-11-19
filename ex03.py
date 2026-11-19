def fun(n):
    x = 1
    for i in range(1,n+1):
        x*=i
    print(f"{n}!={x}")
fun(4)