

def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit."""
    if not isinstance(celsius, (int, float)):
        raise ValueError("A temperatura deve ser um número.")
    return (celsius * 9/5) + 32
