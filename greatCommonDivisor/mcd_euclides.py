def mcd_euclides(a, b):
    """
    Calcula el MCD de dos números utilizando el Algoritmo de Euclides recursivo.

    :param a: Primer número entero
    :param b: Segundo número entero
    :return: MCD de a y b
    """
    if b == 0:
        return a
    else:
        return mcd_euclides(b, a % b) 
          # a%b es el modulo (o resto) de a mod b

# Ejemplo de uso
print(mcd_euclides(30, 21))  
  # Debería devolver 3
