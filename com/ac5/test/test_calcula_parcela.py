import pytest
from com.ac5.calcula_parcela import valorPagamento

def test_valorCerto():
    assert valorPagamento(8 , 5) == 8.64, "Deveria ser 8.64"


def test_valorMenor():
    assert valorPagamento(-2 , 5) == None, "Deveria ser None"


def test_diaZero():
    assert valorPagamento(10 , 0) == 10, "Deveria ser 5"