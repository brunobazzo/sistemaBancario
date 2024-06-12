
class Cliente():
    
    def __init__(self, endereco):
        self._endereco = endereco
        self.contas = []


    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        pass
    
    def adicionar_conta(self, conta):
        self._conta.append(conta)

