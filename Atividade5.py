
import random

class Conta:
    def __init__(self, agencia, conta, proprietario, renda, saldo, limite):
        self.agencia = agencia;
        self.conta = conta;
        self.proprietario = proprietario;
        self.renda = renda;
        self.saldo = saldo;
        self.limite = limite;
    
    
    def saque(self, valor):
        self.saldo -= self.valor;
    
    def deposito(self, valor):
        self.saldo += self.valor;
    
    def consultaSaldo(self):
        print(f"Saldo: R$ {self.saldo}");
    
    def consultaLimite(self):
        print(f"Limite = R$ {self.limite}")
    
    def saqueLimite(self, valor):
        limite -= (valor + (valor*0.0199))

agencia = int(input("Digite o numero da agencia: "))
conta = random.randint(0, 9999)
proprietario = input("Digite o nome do titular da conta: ")
renda = float(input("Digite a renda mensal do titular: "))
saldo = float(input("Digite o saldo inicial da conta: "))
limite = round(random.uniform(renda, (renda*2)));


novaConta = Conta(agencia, conta, proprietario, renda, saldo, limite)

print("Dados da conta:")
print(f"Agencia: {novaConta.agencia}")
print(f"Conta: {novaConta.conta}")
print(f"Proprietario: {novaConta.proprietario}")
print(f"Renda mensal: {novaConta.renda}")
print(f"Saldo: R$ {novaConta.saldo}")
print(f"Limite especial: R$ {novaConta.limite}")