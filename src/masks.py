def mask_card(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает его маску
    """
    masked_card = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[12:]
    return masked_card


def mask_count(count_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску
    """
    masked_count = "**" + count_number[16:20]
    return masked_count
