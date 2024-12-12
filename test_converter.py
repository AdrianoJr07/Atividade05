

import pytest
from converter import celsius_para_fahrenheit

def test_celsius_para_fahrenheit():
    # Testes básicos
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(-40) == -40

    # Teste com valores decimais
    assert celsius_para_fahrenheit(37.5) == pytest.approx(99.5, 0.1)

    # Teste de erros
    with pytest.raises(ValueError):
        celsius_para_fahrenheit("abc")
    with pytest.raises(ValueError):
        celsius_para_fahrenheit(None)
