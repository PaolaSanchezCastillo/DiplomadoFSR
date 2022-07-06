## Formas de descomposicion de problemas


## Procedimental

# El claro ejemplo es C, basicamente el codigo se barre de la parte superior a la 
#inferior del software, es dificil mantener un control
# se usa para programacion de hardware o S.O

## Declarativos
## Alto nivel (Son mas cercanos al lenguaje humano)
## SQL 

## Orientados a objetos
## JAVA 
## Bases de la POO 
## Herencia, Abstraccion, Encapsulamiento, Polimorfismo 

## Funcional 
## Recursividad 
## Funciones
## Caja negra, que recibe y/o/no regresa resultado 


#La siguiente es una forma de declarar e invocar una simple funcion

def impresion():
    print("HOLA")

impresion()

def saludo(nombre):
    print("Hola " + nombre)


saludo("Paola")

##saludo(4)


##solucion 1
def suma(num1, num2):
    resultado = str(num1 + num2)
    print("El resultado es " + resultado)


suma(1,4)


## Entrada de datos 

print("Hola, cual es tu nombre")
nombre = input()
print("Hola " + nombre + " gusto en conocerte")



