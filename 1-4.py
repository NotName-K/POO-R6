def mayor_suma(lista):
    try:
        if not lista:
            raise EntradaInvalidaError("La lista no puede estar vacía.")
        if not all(isinstance(x, (int, float)) for x in lista):
            raise EntradaInvalidaError("Todos los elementos deben ser números.")

        max_suma = actual = lista[0]
        for num in lista[1:]:
            actual = max(num, actual + num)
            max_suma = max(max_suma, actual)
        return max_suma
    except Exception as e:
        print(f"Error en mayor_suma: {e}")
        return None


if __name__ == "__main__":
    try:
        print(mayor_suma([1, -2, 3, 4, -1, 2, 1, -5, 4]))
        print(mayor_suma([]))
    except EntradaInvalidaError as e:
        print(f"Error: {e}")