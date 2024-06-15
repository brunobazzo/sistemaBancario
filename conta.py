
from datetime import datetime
from historico import Historico


class Conta():
    
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "001"
        self._cliente = cliente
        self._historico = Historico()
        self.saques = 0


    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)

    def sacar(self, valor):
        if (valor <= self._saldo and valor > 0):
            hoje = datetime.now()
            self.saques = 0
            for transacao in self.historico.transacoes:
                if transacao['data'].date() == hoje.date():
                    self.saques += 1

            if self.saques >= 10:
                return False
            else:
                self._saldo -= valor
            return True
        else:
            return False


    def depositar(self, valor):
        if(valor > 0):
            self._saldo += valor
            return True
        else:
            return False