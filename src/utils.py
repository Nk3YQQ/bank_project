import json
from typing import Any


def get_transactions(file_path: str = "data/operations.json") -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def get_transaction_on_rub(transaction: dict) -> float | ValueError:
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])
    if currency == "RUB":
        return amount
    else:
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
