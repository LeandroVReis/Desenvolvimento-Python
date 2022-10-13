#import contas_bancos as cb
from agencia import AgenciaComum, AgenciaPremium, AgenciaVirtual
from contas_bancos import ContaCorrente, CartaoCredito
import time

#programa
conta_lvr = ContaCorrente("Leandro Vasconcelos", "123.456.789-00", 1234, 10001)
conta_leo = ContaCorrente('Leandro Reis','987.654.321-00', 1234, 10002)

#depositando valor
conta_lvr.depositar(1000)

#aguardando 3s
time.sleep(3)

#sacando valor
conta_lvr.sacar_dinheiro(1100)
print()

#aguardando 3s
time.sleep(2)

#transferindo pra outra conta
conta_lvr.transferir(150, conta_leo)
print()

#consultando valores atuais e histórico das contas
conta_lvr.consultar_saldo()
conta_lvr.consultar_limite_chequeespecial()
conta_lvr.consultar_historico()
print()

conta_leo.consultar_saldo()
conta_leo.consultar_limite_chequeespecial()
conta_leo.consultar_historico()
print()

#cadastrando Cartão de Crédito
cartao_lvr = CartaoCredito('Leandro Vasconcelos',conta_lvr)
cartao_lvr.senha = '1424'

# print(cartao_lvr.conta_corrente._num_conta)
# print(conta_lvr.cartoes[0].numero)
# print(cartao_lvr.validade)
# print(cartao_lvr.cod_seguranca)
# print(cartao_lvr.senha)
# print()

#imprimindo o conteudo das classes
# print(conta_lvr.__dict__)
# print(cartao_lvr.__dict__)

agencia_virtual_top = AgenciaVirtual('www.agenciavirtual.com.br',33335555)
agencia_virtual_top.verificar_caixa()
print()