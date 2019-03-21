def fibonacci(n):
    """Questa funzione calcola la serie di fibonacci fino al
       valore n inserito.
    ===========================

    Params:
        n: estremo della serie di Fibonacci (int):
    Returns:
        None
    """
    a,b=0,1
    while a < n:
        print(a, end=' ')
        c = b+a
        b,a=a,c

def fibonacci_2(n):
    a,b=0,1
    fib=[]
    while a<n:
        fib.append(a)
        c=b+a
        b,a=a,c
    return fib

if __name__ == '__main__':
    res = fibonacci(15) # the def has no return, res is None
    res_2 = fibonacci_2(n=15)
    print(res)
    print(res_2)
