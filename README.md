# POO-R6
## Logo del grupo
![Logo](https://github.com/NotName-K/POO-R2/blob/main/Screenshot%202025-09-23%20110719.png?raw=true)
## 5 puntos de pdc, con exceptions.
### 1. Operaciones basicas con entrada (1,2,"+")
```python
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
````
### 2. Palindromos
```python
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

```
### 3.Numeros Primos
```python
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
            if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
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
```

### 4. Mayor suma de consecutivos 
```python
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
```

### 5. Palabras con mismos caracteres
```python
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
        print(mismas_letras("amor", "roma"))     # True
        print(mismas_letras("hola", 123))        # Error
    except EntradaInvalidaError as e:
        print(f"Error: {e}")
```
## Shape() con exceptions.
Se crea una excepción propia:
```python
class GeometryError(Exception):
    "Error general para operaciones geométricas inválidas."
    def __init__(self, mensaje="Error en operación geométrica"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

```
Y Se modifican las funciones, agregando el exception antes mencionado, por ejemplo: 
````python
if not all(isinstance(v, (int, float)) for v in [x, y]):
    raise GeometryError("Las coordenadas deben ser numéricas.")

if length <= 0 or width <= 0:
    raise GeometryError("Largo y ancho deben ser positivos.")

## Esto evita crear figuras con datos inválidos antes de que ocurra un error silencioso.
````

```python
try:
    s = self.compute_perimeter() / 2
    return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))
except ValueError:
    raise GeometryError("Error al calcular el área. Verifique los lados.")
## Si los lados no forman un triángulo válido (o dan raíz negativa), se lanza un GeometryError con un mensaje claro.
```
