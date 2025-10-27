class CuentaBancaria():
    def __init__(self):
        self.saldo = 0
        self.cliente = ""

    ## Defino setters y getters para el saldo
    def setSaldo(self,nuevosaldo):
        self.__saldo = nuevosaldo
    def getSaldo(self):
        return self.__saldo

cuentacliente1 = CuentaBancaria()
cuentacliente1.setSaldo(78000000)
print(cuentacliente1.getSaldo())
