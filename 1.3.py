def primos(lista):
    try:
        if not isinstance(lista, list):
            raise EntradaInvalidaError("Debe ingresar una lista de números.")
        if not all(isinstance(x, int) for x in lista):
            raise EntradaInvalidaError("Todos los elementos deben ser enteros.")

        primos = []
        for n in lista:
            if n < 2:
                continue
            if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)):
                primos.append(n)
        return primos
    except Exception as e:
        print(f"Error calculando primos: {e}")
        return []


if __name__ == "__main__":
    try:
        print(primos([1, 2, 3, 4, 5, 7, 10, "a"]))
    except EntradaInvalidaError as e:
        print(f"Error: {e}")
