from collections import defaultdict
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


def avg_cost_and_quantity(list_: list[dict]) -> dict:
    """
    Функция принимает на вход список словарей, представляющих информацию о заказах в интернет-магазине и
    возвращает словарь, содержащий информацию о средней стоимости заказа и количестве заказов за каждый месяц
    """
    monthly_stats = defaultdict(lambda: {"total_value": 0, "order_count": 0})

    for order in list_:
        order_date = order["date"]
        order_items = order["items"]

        year_month = order_date[:7]

        total_order_value = sum(item["price"] for item in order_items)

        monthly_stats[year_month]["total_value"] += total_order_value
        monthly_stats[year_month]["order_count"] += 1

    statistic = {}
    for year_month, data in monthly_stats.items():
        average_order_value = data["total_value"] / data["order_count"]
        order_count = data["order_count"]
        statistic[year_month] = {"average_order_value": average_order_value, "order_count": order_count}

    return statistic
