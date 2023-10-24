def mask_card(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает его маску
    """
    if len(card_number) != 16 or card_number.isdigit() is False:
        return "Некорректный номер карты"

    masked_card = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[12:]
    return masked_card


def mask_count(count_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску
    """
    count_number = str(count_number)
    if len(count_number) != 20 or count_number.isdigit() is False:
        return "Некорректный номер счёта"

    masked_count = "**" + count_number[16:20]
    return masked_count
