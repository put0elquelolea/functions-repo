import random
def num_aleatorios(n):
      lista = [0] * n
      for i in range(n):
          lista[i] = random.randint(0, 10000)
      return lista

n=int(input("Ingrese cuantos numeros aleatorios desea obtener " ))

aleatorios = num_aleatorios(n)
print(aleatorios)
