def es_palindromo(palabra: str) -> bool:
    try:
        if not isinstance(palabra, str):
            raise EntradaInvalidaError("La palabra debe ser una cadena.")
        palabra = palabra.lower().replace(" ", "")
        return palabra == palabra[::-1]
    except Exception as e:
        print(f"Error en es_palindromo: {e}")
        return False

if __name__ == "__main__":
    try:
        print(es_palindromo("Anita lava la tina"))
        print(es_palindromo(12345))
    except EntradaInvalidaError as e:
        print(f"Error: {e}")
