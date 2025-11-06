def mismas_letras(p1: str, p2: str) -> bool:
    try:
        if not all(isinstance(p, str) for p in [p1, p2]):
            raise EntradaInvalidaError("Ambos argumentos deben ser cadenas.")

        return sorted(p1.replace(" ", "").lower()) == sorted(p2.replace(" ", "").lower())
    except Exception as e:
        print(f"Error en mismas_letras: {e}")
        return False


if __name__ == "__main__":
    try:
        print(mismas_letras("amor", "roma"))  # True
        print(mismas_letras("hola", 123))  # Error
    except EntradaInvalidaError as e:
        print(f"Error: {e}")