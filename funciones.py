
import random
min = int(input("introduce tu rango menor "))
max = int(input("introduce tu rango maximo "))

def num_aleatorios(n):
      lista = [0] * n
      for i in range(n):
          lista[i] = random.randint(min, max)
                    
      return lista

n=int(input("Ingrese cuantos numeros aleatorios desea obtener " ))

aleatorios = num_aleatorios(n)
print(aleatorios)

def suma(num_1, num_2):
   sum = num_1 + num_2
   return sum

def resta(num_1, num_2):
    res = num_2 - num_1
    return res

def multiplicacion(num_1, num_2):
    mul = num_1 * num_2
    return mul

def division(num_1, num_2):
    div = num_2/num_1
    return div


menu = """
estas son tus opciones:
1-deseas sumarlos?
2-deseas restarlo?
3-deseas multiplicarlos?
4-deseas divirlos?
5-deseas salir?
"""

num_1 = int(input("introduce tu primer valor, por favor introduce el menor de los valores "))
num_2 = int(input("introduce tu segundo valor, por favor introduce el mayor de los valores"))

if num_1 and num_2 > 0:
    print(menu)
else:
    print("error al introducir valores vuelve a intentar")

while True:
    op = int(input("elige una opcion "))
    if op == 1:
        resultado = suma(num_1, num_2)
        print(resultado)
    elif op == 2:
        resultado = resta(num_1, num_2)
        print(resultado)
    elif op == 3:
        resultado = multiplicacion(num_1, num_2)
        print(resultado)
    elif op == 4:
        resultado = division(num_1, num_2)
        print(resultado)
    elif op == 5:
        break
    else:
        print("error al introducir valores, vulve a intentar...")
    
        
