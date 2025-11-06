def sumar(a, b):
    try:
        return a + b
    except TypeError:
        raise EntradaInvalidaError("Ambos valores deben ser numéricos.")

def restar(a, b):
    try:
        return a - b
    except TypeError:
        raise EntradaInvalidaError("Ambos valores deben ser numéricos.")

def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        raise EntradaInvalidaError("Ambos valores deben ser numéricos.")

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise EntradaInvalidaError("No se puede dividir entre cero.")
    except TypeError:
        raise EntradaInvalidaError("Ambos valores deben ser numéricos.")

if __name__ == "__main__":
    try:
        print(dividir(10, 0))
    except EntradaInvalidaError as e:
        print(f"Error: {e}")