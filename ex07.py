def fun1(n):
    if n==1:
        return 1
    else:
        return n*fun1(n-1)