from typing import Optional


def get_list_with_state(list_: list[dict], value: Optional[str] = None) -> list[dict]:
    """
    Функцию принимает на вход список словарей и значение для ключа state и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение
    """
    if value == "CANCELED":
        return [element for element in list_ if element["state"] == "CANCELED"]
    return [element for element in list_ if element["state"] == "EXECUTED"]


def sort_list_by_date(list_: list[dict], desc: bool = False) -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы
    по убыванию даты (если параметр desc == True).
    """
    if desc is True:
        return sorted(list_, key=lambda x: x["date"], reverse=desc)
    return sorted(list_, key=lambda x: x["date"])


def sort_list_by_price(list_: list[dict], category: Optional[str] = None) -> list[dict]:
    """
    Функция принимает на вход список словарей, состоящих из данных о продуктах в магазине и
    возвращает список словарей, отсортированных по убыванию стоимости продукта, но только для
    продуктов из заданной категории. Если категория не задана, то сортировка производится для всех продуктов.
    """
    sorted_list = sorted(list_, key=lambda x: x["price"], reverse=True)
    if category is not None and category in [product["category"] for product in sorted_list]:
        return [product for product in sorted_list if category in product["category"]]
    return sorted_list
