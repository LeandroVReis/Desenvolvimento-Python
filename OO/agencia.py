from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            texto = 'Caixa abaixo do nível recomendando!!! Caixa atual: R${:_.2f}'.format(self.caixa)
            texto = texto.replace('.', ',').replace('_', '.')
            print(texto)
        else:
            texto = 'O valor de caixa está OK!!! Caixa atual: R${:_.2f}'.format(self.caixa)
            texto = texto.replace('.', ',').replace('_', '.')
            print(texto)

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível de ser realizado! Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


#SUB-CLASSES

#AgenciaVirtual
class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone):
        super().__init__(telefone, 12345678000199, 1000)
        self.caixa = 1000000
        self.site = site
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor

#AgenciaComum
class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001,9998))
        self.caixa = 10000000

#AgenciaPremium
class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001,9998))
        self.caixa = 100000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O Cliente não tem o patrimônio mínimo necessário para entrar na Agência Premium!')


if __name__ == '__main__':
    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br',33335555)
    agencia_virtual.verificar_caixa()
    print()

    agencia_comum = AgenciaComum(33331111, 12345678000137)
    agencia_comum.verificar_caixa()
    print()

    agencia_premium = AgenciaPremium(33333333, 12345678000120)
    agencia_premium.verificar_caixa()
    print()

    agencia_virtual.depositar_paypal(30000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    agencia_premium.adicionar_cliente('Leandro Vasconcelos', 98765432100, 1500000)
    print(agencia_premium.clientes)

    agencia_comum.adicionar_cliente('Leoswaldo', 45678932100, 150)
    print(agencia_comum.clientes)

# agencia1 = Agencia(33330000, 12345678000100, 9999)
# agencia1.caixa = 999999999
# agencia1.verificar_caixa()
# print()
#agencia1.emprestar_dinheiro(1500, 12345678900, 0.02)
#print(agencia1.emprestimos)
#agencia1.adicionar_cliente('Leandro Vasconcelos', 98765432100, 15000)
#print(agencia1.clientes)
