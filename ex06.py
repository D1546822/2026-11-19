def menu():
    print()
    
def fun1():
    a = int(input("a="))
    b = int(input("b="))
    result = a**b
    print(f"{a}的{b}次方={result}")
    
def fun21(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans+i
    return ans
def fun2(n,m):
n,m = map(int,input().split())
print(fun21(n)/(fun21(m)*fun2/(n-m)))

def fun3(f):
    c = (f-32)*5/9
    return c

def main():
    while True:
        menu()
        op = input()
        if op==1:
            fun1()
        elif op==2:
            fun2()
        elif op==3:
            f = float(input())
            c = fun3(f)
            print(c)
        else:
            break