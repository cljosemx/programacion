print('Menu de aplicaciones')
print('1) Tablas de multiplicar')
print('2) Calculadora básica')
print('3) Serie de números')
print('4) Comparar dos números')
print('5) Comparar dos áreas de rectángulos')
print('***********Selecciona y escribe una opción: ***********')
O=int(input())
if O==1:
    print("Escribe la tabla de multiplicar deseada")
    T=int(input())
    for i in range(1, 11, 1):
        print(T,"x",i,"=",T*i)
elif O==2:
    print('Escribe el primer número')
    A=int(input())
    print('Escribe el segundo número')
    B=int(input())
    print('Selecciona una opción: S para suma, R para resta, M para multiplicación y D para división')
    op=str(input())
    if op=='S':
        print('La suma es:', A+B)
    elif op=='R':
        print('La resta es:', A-B)
    elif op=='M':
        print('La multiplicación es:', A*B)
    elif op=='D':
        print('La división es:', A/B)
    else:
        print('No tengo esa opción')
elif O==3:
    print('Escribe el inicio del ciclo')
    i=int(input())
    print('Escribe el límite del ciclo')
    L=int(input())
    print('Escribe el incremento del ciclo')
    inc=int(input())
    for X in range(i,L,inc):
        print(X)
elif O==4:
    print('Escribe el valor de A')
    A=int(input())
    print('Escribe el valor de B')
    B=int(input())
    if A>B:
        print('A es mayor que B')
    else:
        print('B es mayor que A')
elif O==5:
    print