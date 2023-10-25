from masks import mask_card, mask_count


def mask_card_with_name(name: str, number: str) -> str:
    """
    Функция принимает на вход строку информацией тип карты/счета и номер карты/счета
    и возвращает эту строку с замаскированным номером карты/счет
    """
    if len(number) == 16 and number.isdigit() is True:
        return f"{name} {mask_card(number)}"
    elif len(number) == 20 and number.isdigit() is True:
        return f"{name} {mask_count(number)}"
    else:
        return "Некорректный номер карты/счёта"
