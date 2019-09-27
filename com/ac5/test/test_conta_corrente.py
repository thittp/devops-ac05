import pytest 
from com.ac5.conta_corrente import ContaCorrente

def test_dep():
   conta = ContaCorrente(10, 'Erick')
   conta.deposito(10)
   assert conta.saldo == 10

def test_saque():
   conta = ContaCorrente(20, 'Thiago', 5)
   conta.saque(5)
   assert conta.saldo == 0