def fibo(n):

    a=0
    b=1
    while a <= n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
    
    print()
    

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y
