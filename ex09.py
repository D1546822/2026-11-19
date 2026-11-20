def fun1(n):
    if n==0 or n==1:
        return n
    else:
        return fun1(n-2)+fun1(n-1)