# Last updated: 3/30/2025, 1:38:57 PM
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ''' 
        if num == 0:
            return 0
        return 1 + self.numberOfSteps(num - 1 if num & 1 else num >> 1)
        '''
        # Si se pasa a binario corresponderia con bit shift a la derecha y sumar 1
        # Por lo cual si cuentas en length en binario mas el numeros de 1 obtienes el total
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()
        

        