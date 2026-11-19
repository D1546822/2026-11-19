def fun1(n, c):
    for i in range(n):
        for j in range(i+1):
            print(c, end=" ")
        print()

n = int(input())
c = input()
fun1(n, c)