import logging

logger = logging.getLogger(__name__)


def mask_card(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает его маску
    """
    masked_card = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[12:]
    logger.info("mask_card is working. Status: ok")
    return masked_card


def mask_count(count_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску
    """
    masked_count = "**" + count_number[16:20]
    logger.info("mask_card is working. Status: ok")
    return masked_count


logger.info("mask.py is working. Status: ok")
