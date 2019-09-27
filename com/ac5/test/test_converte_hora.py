import pytest
from com.ac5.cvHora import converteHora


def test_convertHora():
    assert converteHora(20, 50) == '08:50 PM', ("O resultado tem que ser 08:50 PM")
    assert converteHora(60, 70) == None, ("O resultado tem que ser None")
    assert converteHora(11, 30) == '11:30 AM', ("O resultado tem que ser 11:30 AM")
    assert converteHora(0, 0) == '12:00 AM', ("O resultado tem que ser 12:00 AM")