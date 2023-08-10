def fibo(n):

    a=0
    b=1
    while a <= n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
    
    print()
    
print(fibo(8))
print(fibo(2))