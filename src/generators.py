from typing import Any, Generator


def get_data() -> list[dict] | Any:
    """
    Функция принимает данные из файла data/transactions.json
    и преобразует их в список словарей
    :return: Список с данными транзакций
    """
    import json

    with open("data/transactions.json") as file:
        data = json.load(file)
        return data


transactions = get_data()


def filter_by_currency(data: list[dict], currency: str) -> Generator:
    """
    Функция принимает список словарей, и возвращает итератор,
    который выдает по очереди операции с заданной валютой.
    :param data:
    :param currency:
    :return: Generator:
    """
    for element in data:
        if element["operationAmount"]["currency"]["code"] == currency:
            yield element


def transaction_descriptions(data: list[dict]) -> Generator:
    """
    Функция принимает список словарей и возвращает описание каждой операции по очереди
    :param data:
    :return: Generator:
    """
    for element in data:
        yield element["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Функция генерирует номера карт. Должны быть сгенерированы номера карт
    в заданном диапазоне, например, от 0000 0000 0000 0001 до 9999 9999 9999 9999
    (диапазоны передаются как параметры генератора).
    :param start:
    :param end:
    :return: Generator
    """
    for num in range(start, end + 1):
        card_num = f"{num:016d}"
        formatted_card_number = " ".join([card_num[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number


def non_empty_truths(list_: list) -> list:
    return [
        [item for item in inner_lst if item is not None and item is not False and item != "" and item != 0]
        for inner_lst in list_
        if any(item for item in inner_lst if item is not None and item is not False and item != "" and item != 0)
    ]
