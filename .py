def calculator(x):
    import math
    def addition(a,b):
        """This is addition"""
        print(a+b)
    def substraction(a,b):
        """This is substraction"""
        print(a-b)
    def multiplication(a,b):
            """This is multiplication"""
            print(a*b)
    def division(a,b):
        """This is division"""
        print(a/b)
    def remainder(a,b):
        """This is remainder"""
        print(a%b)
    def root(a,b):
        """This is root"""
        print(a**(1/b))
    def exponent(a,b):
        """This is exponent"""
        print(pow(a,b))
    def sine(a):
        """This is sin in degrees"""
        print(math.sin(math.radians(a)))
    def cosine(a):
        """This is cos in degrees"""
        print(math.cos(math.radians(a)))
    def sine1(a):
        """This is sin in radians"""
        print(math.sin(math.degrees(a)))
    def cosine1(a):
        """This is cos in radians"""
        print(math.cos(math.degrees(a)))
    def tangent(a):
        """This is tan in degrees"""
        print(math.tan(math.radians(a)))
    def tangent1(a):
        """This is tan in radians"""
        print(math.tan(math.degrees(a)))
    a=eval(input("Enter the value of a: "))
    b=eval(input("Enter the value of b (0 for degrees 1 for radians): "))
    n=input("Enter\n + for addition\n - for substraction\n * for multiplication\n / for division\n % for remaindeer\n ** for exponent\n sin for sine\n cos for cosine\n tan for tangent\n 0 for square root : ")
    if n=="+":
        print(addition.__doc__)
        addition(a,b)
    elif n=="-":
        print(substraction.__doc__)
        substraction(a, b)
    elif n=="*":
        print(multiplication.__doc__)
        multiplication(a, b)
    elif n=="/":
        print(division.__doc__)
        division(a, b)
    elif n=="%":
        print(remainder.__doc__)
        remainder(a, b)
    elif n=="**":
        print(exponent.__doc__)
        exponent(a,b)
    elif n=="sin":
        if b==1:
            print(sine1.__doc__)
            sine1(a)
        else:
            print(sine.__doc__)
            sine(a)
    elif n=="cos":
        if b==1:
            print(cosine1.__doc__)
            cosine1(a)
        else:
            print(cosine.__doc__)
            cosine(a)
    elif n=="tan":
        if b==1:
            print(tangent1(a).__doc__)
            tangent1(a)
        else:
            print(tangent.__doc__)
            tangent(a)
    elif n=="0":
        print(root.__doc__)
        root(a,b)
    else:
        print("Enter a correct operator")
while True:
    x=input("Enter (y/Y) to run calc or (n/N) to exit: ")
    if x=="Y" or x=="y":
        calculator(x)
    elif x=="n" or x=="N":
        exit()
    else:
        print("Enter the correct value")
