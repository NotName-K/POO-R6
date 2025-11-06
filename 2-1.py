import math

class GeometryError(Exception):
    """Error general para operaciones geométricas inválidas."""
    def __init__(self, mensaje="Error en operación geométrica"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class Point:
    def __init__(self, x: float, y: float):
        try:
            if not all(isinstance(v, (int, float)) for v in [x, y]):
                raise GeometryError("Las coordenadas deben ser numéricas.")
            self.__x = x
            self.__y = y
        except Exception as e:
            raise GeometryError(f"Error al crear el punto: {e}")

    def get_x(self):
        return self.__x

    def set_x(self, value):
        if not isinstance(value, (int, float)):
            raise GeometryError("El valor de x debe ser numérico.")
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        if not isinstance(value, (int, float)):
            raise GeometryError("El valor de y debe ser numérico.")
        self.__y = value

    def compute_distance(self, point: "Point") -> float:
        if not isinstance(point, Point):
            raise GeometryError("El argumento debe ser una instancia de Point.")
        return ((self.__x - point.get_x()) ** 2 + (self.__y - point.get_y()) ** 2) ** 0.5



class Line:
    def __init__(self, p_s: Point, p_e: Point):
        try:
            if not all(isinstance(p, Point) for p in [p_s, p_e]):
                raise GeometryError("Los extremos deben ser objetos Point.")
            self.__p_s = p_s
            self.__p_e = p_e
            self.__update_length()
        except Exception as e:
            raise GeometryError(f"Error al crear la línea: {e}")

    def get_start_point(self):
        return self.__p_s

    def set_start_point(self, p_s: Point):
        if not isinstance(p_s, Point):
            raise GeometryError("El punto inicial debe ser un Point.")
        self.__p_s = p_s
        self.__update_length()

    def get_end_point(self):
        return self.__p_e

    def set_end_point(self, p_e: Point):
        if not isinstance(p_e, Point):
            raise GeometryError("El punto final debe ser un Point.")
        self.__p_e = p_e
        self.__update_length()

    def get_length(self):
        return self.__length

    def __update_length(self):
        self.__length = self.__p_s.compute_distance(self.__p_e)



class Shape:
    def __init__(self, vertices=None, edges=None, inner_angles=None, is_regular=False):
        self.__vertices = vertices or []
        self.__edges = edges or []
        self.__inner_angles = inner_angles or []
        self.__is_regular = is_regular

    def get_vertices(self):
        return self.__vertices

    def set_vertices(self, vertices):
        if not isinstance(vertices, list):
            raise GeometryError("Los vértices deben ser una lista.")
        self.__vertices = vertices

    def get_edges(self):
        return self.__edges

    def set_edges(self, edges):
        if not isinstance(edges, list):
            raise GeometryError("Los bordes deben ser una lista.")
        self.__edges = edges

    def get_inner_angles(self):
        return self.__inner_angles

    def set_inner_angles(self, angles):
        if not isinstance(angles, list):
            raise GeometryError("Los ángulos deben ser una lista.")
        self.__inner_angles = angles

    def get_is_regular(self):
        return self.__is_regular

    def set_is_regular(self, value):
        if not isinstance(value, bool):
            raise GeometryError("El valor de regularidad debe ser booleano.")
        self.__is_regular = value

    def compute_area(self):
        raise NotImplementedError("Método implementado por la subclase")

    def compute_perimeter(self):
        raise NotImplementedError("Método implementado por la subclase")

    def compute_inner_angles(self):
        raise NotImplementedError("Método implementado por la subclase")



class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        if not all(isinstance(v, (int, float)) for v in [length, width]):
            raise GeometryError("Largo y ancho deben ser numéricos.")
        if length <= 0 or width <= 0:
            raise GeometryError("Largo y ancho deben ser positivos.")

        self.__length = length
        self.__width = width

        vertices = [
            Point(0, 0),
            Point(length, 0),
            Point(length, width),
            Point(0, width)
        ]
        super().__init__(vertices, is_regular=False)

    def get_length(self):
        return self.__length

    def set_length(self, value):
        if value <= 0:
            raise GeometryError("El largo debe ser positivo.")
        self.__length = value

    def get_width(self):
        return self.__width

    def set_width(self, value):
        if value <= 0:
            raise GeometryError("El ancho debe ser positivo.")
        self.__width = value

    def compute_area(self):
        return self.__length * self.__width

    def compute_perimeter(self):
        return 2 * (self.__length + self.__width)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]



class Square(Rectangle):
    def __init__(self, side: float):
        if not isinstance(side, (int, float)) or side <= 0:
            raise GeometryError("El lado debe ser un número positivo.")
        super().__init__(side, side)
        self.set_is_regular(True)

    def compute_area(self):
        side = self.get_length()
        return side ** 2

    def compute_perimeter(self):
        return 4 * self.get_length()



class Triangle(Shape):
    def __init__(self, a, b, c):
        if not all(isinstance(x, (int, float)) for x in [a, b, c]):
            raise GeometryError("Los lados deben ser numéricos.")
        if not (a + b > c and a + c > b and b + c > a):
            raise GeometryError("Los lados no forman un triángulo válido.")
        self.__a = a
        self.__b = b
        self.__c = c
        super().__init__(is_regular=False)

    def get_sides(self):
        return self.__a, self.__b, self.__c

    def compute_perimeter(self):
        return self.__a + self.__b + self.__c

    def compute_area(self):
        try:
            s = self.compute_perimeter() / 2
            return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))
        except ValueError:
            raise GeometryError("Error al calcular el área. Verifique los lados.")

    def compute_inner_angles(self):
        a, b, c = self.get_sides()
        try:
            A = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
            B = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
            C = 180 - A - B
            return [A, B, C]
        except ValueError:
            raise GeometryError("Error al calcular los ángulos internos.")


class Isosceles(Triangle):
    def __init__(self, equal_side, base):
        super().__init__(equal_side, equal_side, base)

    def compute_area(self):
        base = self.get_sides()[2]
        equal = self.get_sides()[0]
        if base >= 2 * equal:
            raise GeometryError("La base es demasiado grande para formar un isósceles válido.")
        height = math.sqrt(equal ** 2 - (base ** 2) / 4)
        return (base * height) / 2


class Equilateral(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.set_is_regular(True)

    def compute_area(self):
        a = self.get_sides()[0]
        return (math.sqrt(3) / 4) * (a ** 2)


class Scalene(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)


class RightTriangle(Triangle):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise GeometryError("Base y altura deben ser positivas.")
        hypotenuse = math.sqrt(base ** 2 + height ** 2)
        super().__init__(base, height, hypotenuse)

    def compute_area(self):
        return (self.get_sides()[0] * self.get_sides()[1]) / 2



if __name__ == "__main__":
    try:
        shapes = [
            Rectangle(4, 2),
            Square(3),
            Triangle(3, 4, 5),
            Equilateral(4),
            RightTriangle(3, 4)
        ]
        for s in shapes:
            print(f"{s.__class__.__name__}: Área={s.compute_area():.2f}, Perímetro={s.compute_perimeter():.2f}")
    except GeometryError as e:
        print(f"Error geométrico: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
