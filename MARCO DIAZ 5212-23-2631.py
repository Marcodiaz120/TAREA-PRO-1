MARCO DIAZ 5212-23-2631


a=float(input("Ingrese el valor de A: "))
b=float(input("Ingrese el valor de B: "))
c=float(input("Ingrese el valor de C: "))

disc=(b**2-4*a*c)
raiz=(disc**0.5)

ra1=(-b+raiz)
sol1=(ra1/2*a)

ra2=(-b-raiz)
sol2=(ra2/2*a)

print("La primera solución es: ", sol1)
print("La segunda solución es: ", sol2)


