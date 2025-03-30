# Last updated: 3/30/2025, 1:32:39 PM
# Esta olucion corresponde con saber que si se pasa a binario se puede ejecutar más rápido.
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Si se pasa a binario corresponderia con bit shift a la derecha y sumar 1
        # Por lo cualsi cuentas en length en binario mas el numeros de 1 obtienes el total
        binary = bin(num)[2:]
        return len(binary)+ binary.count('1')-1
        