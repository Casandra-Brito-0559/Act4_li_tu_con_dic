arcoiris=("Azul","Verde","Rojo","Amarillo","Morado","Naranja")
print(arcoiris)
print("--Longitud de arcoiris--")
print(len(arcoiris))

animales=("Pantera",20,"estatura",1.7)
print(animales)
print("elementos de la tupla")
print(arcoiris[1:3])


x = ("Io", "Kevin", "Tifany")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

print("Agregando elementos")
nanimal=("Boby","chetos")


y = list(nanimal)
y.append("tontolin")
otratupla = tuple(y)
print(otratupla)

print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)