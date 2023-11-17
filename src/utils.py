import json
import logging
from typing import Any

logger = logging.getLogger(__name__)


def get_transactions(file_path: str = "../data/operations.json") -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info("get_transactions is working. Status: ok")
            return data
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        logger.error("FileNotFoundError/json.decoder.JSONDecodeError")
        return []


def get_transaction_on_rub(transaction: dict) -> float | ValueError:
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])
    if currency == "RUB":
        logger.info("get_transactions_on_rub is working. Status: ok")
        return amount
    else:
        logger.error("ValueError")
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
