# Definimos x como cadena 
x = "El valor de (b+c)*a es"


a, b, c = 5, 2, 10

# operacion con a,b,c
d = (b + c) * a


imprimir = True


if imprimir:
    print(x, d)

    if imprimir:
    print(x, d)

# comentarios 
'''
comentario 
de varias 
lienas 
'''
#Indentación y bloques de código
if True:
   print("si")

if True:
print("NO")
#es incorrec, no se respetan los espacios y no cuente dentro del if

x = 8
y = 77
#python no necesita un ; al final de cada linea de codigo 

f = 30; g = 9; h=79
# con un ; podemos poner dos variables en la misma linea o mas 


#varias  líneas
j = 9 + 7 + 5 + 4 +\
    5 * 6
#con una / se puede prtir una linea de codigo si es muy larga se recomienda no exceder 79 caracteres
k = (8 + 0 + 2 + 4 +
     99 + 70) 
#dentro de una linea de codigo dentro de () se puede partir el codigo igual 


#crear variables :
l = z = 6  # se puede asignar el mismo valor a diferentes variables 

n, v = 4, 2
t, u, o = 1, 2, 3 #podemos asignar varios valores separados por coma


#nombres de variables 
# Válido
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10

# No válido
2variable = 10
var-iable = 10
var iable = 10

#como usar los parentecis 
y = x*3-3**10-2+3  # co doble ** es un exponente :o

y = (x*3-3)**(10-2)+3 # los () dan prioridad a las operaciones que encierran 

#el 10 tiene alcance golbal y el 5 local al imprimir x se accede al valor global 
x = 10

def funcion():
    x = 5

funcion()
print(x)

# uso de print 

print("esto se muestra en pantalla")

#se puede imprimir lo que vale una variable 
x = 10
print(x)

#se puede imprimir los valores de mas de 1 variable con una, 
x = 600
y = 20
print("Los valores x, y son:", x, y)