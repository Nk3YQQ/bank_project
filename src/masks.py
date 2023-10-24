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


def mask_card_with_name(name, number: str | str) -> str | str:
    """
    Функция принимает на вход строку информацией тип карты/счета и номер карты/счета
    и возвращает эту строку с замаскированным номером карты/счет
    """
    if len(number) == 16 and number.isdigit() is True:
        masked_card = number[:4] + " " + number[4:6] + "** " + "**** " + number[12:]
        return f'{name} {masked_card}'
    elif len(number) == 20 and number.isdigit() is True:
        masked_count = "**" + number[16:20]
        return f'{name} {masked_count}'
    else:
        return 'Некорректный номер карты/счёта'


def reformat_date(date_: str) -> str:
    """
    Функцию, которая принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"
    """
    if 0 < int(date_[8:10]) <= 31 and 0 < int(date_[5:7]) <= 12:
        return date_[8:10] + '.' + date_[5:7] + '.' + date_[0:4]
    else:
        return 'Некорректно введена дата'


def search_anagram(list_: list[str]) -> list[str]:
    """
    Функция, которая принимает на вход список строк и возвращает список строк,
    где первая и последняя буквы совпадают. Если список пустой, то функция
    вернёт пустой список.
    """
    if len(list_) == 0:
        return []
    return [element for element in list_ if element[0] == element[-1]]


def return_max_composition(list_: list[int]) -> int:
    """
    Функция, которая принимает на вход список целых чисел и
    возвращает максимальное произведение двух чисел из списка
    """
    list_of_max_count = []
    if len(list_) < 2:
        return 0
    max_count_one = max(list_)
    list_of_max_count.append(max_count_one)
    list_.remove(max_count_one)
    max_count_two = max(list_)
    list_of_max_count.append(max_count_two)
    return list_of_max_count[0] * list_of_max_count[1]
