from datetime import datetime as dt
import pytz
from random import randint

class ContaCorrente():
    """
    Cria uma ContaCorrente para gerenciar todas as operações

    Atributos: PEP 257

    nome (str): Nome do Cliente
    cpf (str):
    """


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = dt.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome  = nome
        self._cpf   = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        texto = 'Seu saldo atual é de R$ {:_.2f}'.format(self._saldo)
        texto = texto.replace('.',',').replace('_','.')
        print(texto)

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        texto = 'Seu limite de Cheque Especial é de R$ {:_.2f}'.format(self._limite_conta())
        texto = texto.replace('.', ',').replace('_', '.')
        print(texto)

    def consultar_historico(self):
        print('Histórico de Transações: Conta:{} CPF:{}'.format(self._num_conta, self._cpf))
        print('+' + ('-' * 7) + '+' + ('-' * 11) + '+' + ('-' * 11) + '+' + ('-' * 21) + '+')
        print('| N.U.M | V.A.L.O.R | S.A.L.D.O |     DATA - HORA     |')
        print('+' + ('-' * 7) + '+' + ('-' * 11) + '+' + ('-' * 11) + '+' + ('-' * 21) + '+')
        for i,item in enumerate(self._transacoes):
            val,sdo,dthr = item
            texto = '|{:^7}| {:>9_.2f} | {:>9_.2f} | {} |'.format(i+1,val,sdo,dthr)
            texto = texto.replace('.', ',').replace('_', '.')
            print(texto)
        print('+' + ('-' * 7) + '+' + ('-' * 11) + '+' + ('-' * 11) + '+' + ('-' * 21) + '+')

    def transferir(self, valor, conta_destino):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para transferir esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = dt.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data().month, CartaoCredito._data().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova Senha Inválida!")

