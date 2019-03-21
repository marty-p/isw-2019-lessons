### FUNZIONI
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

res = fibonacci(15) # the def has no return, res is None
print(res)

def fibonacci_2(n):
    a,b=0,1
    fib=[]
    while a<n:
        fib.append(a)
        c=b+a
        b,a=a,c
    return fib

res_2 = fibonacci_2(n=15)
print(res_2)

def somma(check=True, a=2, b=3):
    if check:
        c=a+b
        return c
    else:
        print("check set to False")

s = somma() #default parameters
print(s)

s_2 = somma(check=False)
print(s_2)

s_3 = somma(a=10, b=20)
print(s_3)



### SCOPE VARIABLES
a= 13 # global var
def niente(b):
    c=b
    d=a
    return c,d

def niente_2(b):
    global c
    return c

















