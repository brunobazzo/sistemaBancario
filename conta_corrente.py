
from conta import Conta


class ContaCorrente(Conta):
    
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques



    def sacar(self, valor):

        numero_saques = 0

        for transacao in self.historico.transacoes:
            if transacao["tipo"] == "Saque":
                numero_saques =+ 1
        
        if numero_saques == self._limite_saques:
            print(f"voce atingiu o numero de saques diario maximo de {self._limite_saques}")
        elif valor > self._limite:
            print(f"voce nao pode sacar o valor {valor} pois é maior que limite{self._limite}")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agencia:\t\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t\t{self.cliente._nome}
        """
