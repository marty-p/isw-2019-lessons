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



### KEYWORDS ARGUMENTS
def presentazione(nome, cognome, eta):
    print("ciao, sono {} {} e ho {} anni".format(nome, cognome, eta))

presentazione("nicola", "uras", 26)
tupla = ("nicola", "uras", 26)

presentazione(*tupla)


def printer(*args):
    for arg in args:
        print(arg)
        
printer('nicola', 'guido', 'elsa', 'jack', 'jacob')


def somma(num_1, num_2, stringa):
    if stringa == 'somma':
        s = num_1 + num_2
        print("La somma dei numeri inseriti è: {}.".format(s))
    else:
        print("non posso calcolare la somma")

dict_args = {"num_1":3, "num_2":5, "stringa":"somma"}
somma(**dict_args)


def printer_2(**args):
    for key in args:
            print(args[key])
printer_2(x=3, y=34, z=-2, t=8)

def printer_3(nome, *args, **kwargs):
    print("mi chiamo {}".format(nome))
    print("\n")
    for arg in args:
        print(arg)
    print("\n")
    for key in kwargs:
        print(kwargs[key])
printer_3('nicola', 'guido', 'elsa', 'jack', x=3, y=-2, z=5)

