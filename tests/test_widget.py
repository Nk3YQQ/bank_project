from src.widget import mask_card_with_name, reformat_date, search_anagram, return_max_composition


def test_mask_card_with_name():
    assert mask_card_with_name('Maestro', '7000792289606361') == 'Maestro 7000 79** **** 6361'
    assert mask_card_with_name('Maestro', '70007922896063') == 'Некорректный номер карты/счёта'
    assert mask_card_with_name('Счет', '64686473678894779589') == 'Счет **9589'
    assert mask_card_with_name('Счет', '6468647367889477958922') == 'Некорректный номер карты/счёта'
    assert mask_card_with_name('', '') == 'Некорректный номер карты/счёта'


def test_reformat_date():
    assert reformat_date('2018-07-11T02:26:18.671407') == '11.07.2018'
    assert reformat_date('2023-10-31T02:26:18.671407') == '31.10.2023'
    assert reformat_date('2023-13-31T02:26:18.671407') == 'Некорректно введена дата'
    assert reformat_date('') == 'Некорректно введена дата'
    assert reformat_date('2018-07-11') == '11.07.2018'


def test_search_anagram():
    assert search_anagram(['hello', 'world', 'apple', 'pear', 'banana', 'pop']) == ['pop']
    assert search_anagram(['madam', 'noon', 'level', '']) == ['madam', 'noon', 'level', '']
    assert search_anagram([]) == []


def test_return_max_composition():
    assert return_max_composition([2, 3, 5, 7, 11]) == 77
    assert return_max_composition([-5, -7, -9, -13]) == 35
    assert return_max_composition([1, 2]) == 2
    assert return_max_composition([4]) == 0
