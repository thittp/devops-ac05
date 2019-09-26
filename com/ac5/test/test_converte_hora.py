import pytest
from com.ac5.cvHora import converteHora


def convertHora():
    assert converteHora(20, 50) == '20:50 PM', ("O resultado tem que ser 20:50 PM")