def sum_divisible_by_3_or_5(list_of_counts: list[int]) -> int:
    """
    Функция принимает на вход список чисел и возвращает сумму всех элементов списка,
    которые делятся на 3 или 5 без остатка.
    """
    result = 0
    for num in list_of_counts:
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


def check_email(email: str) -> bool:
    """Функция проверяет, является ли переданный ей email правильно написанным"""
    return True if "@" in email and "." in email[-4:] else False


def count_number_in_list(list_of_counts: list[int], number: int) -> int:
    """Функция принимает список чисел и число, а также возвращает количество раз,
    когда число встретилось в списке"""
    result = 0
    for num in list_of_counts:
        if num == number:
            result += 1
    return result


def calculate_area(shape: str, sides: list[int]) -> int | None:
    """
    Функция принимает на вход название геометрической фигуры в виде строки и список ее сторон
    (в случае окружности список содержит радиус), а затем возвращает ее площадь
    """
    from math import pi, sqrt

    if not sides:
        return 0
    if shape == "треугольник":
        p = sum(sides) / 2
        square = round(sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])))
        return square
    elif shape == "круг":
        square = round(pi * (sides[0] ** 2))
        return square
    elif shape == "прямоугольник" or shape == "квадрат":
        square = sides[0] * sides[1]
        return square
    else:
        return None
