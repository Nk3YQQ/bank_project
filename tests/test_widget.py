import pytest

from src.widget import mask_card_with_name, reformat_date, return_max_composition, search_anagram


@pytest.mark.parametrize(
    "name, number, expected_result",
    [
        ("Maestro", "7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Maestro", "70007922896063", "Некорректный номер карты/счёта"),
        ("Счет", "64686473678894779589", "Счет **9589"),
        ("Счет ", "3538303347444789556022", "Некорректный номер карты/счёта"),
        ("", "", "Некорректный номер карты/счёта"),
    ],
)
def test_mask_card_with_name(name: str, number: str, expected_result: str) -> None:
    assert mask_card_with_name(name, number) == expected_result


@pytest.mark.parametrize(
    "date_, expected_result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2023-10-31T02:26:18.671407", "31.10.2023"),
        ("2023-13-31T02:26:18.671407", "Некорректно введена дата"),
        ("", "Некорректно введена дата"),
        ("2018-07-11", "11.07.2018"),
    ],
)
def test_reformat_date(date_: str, expected_result: str) -> None:
    assert reformat_date(date_) == expected_result


@pytest.mark.parametrize(
    "list_, expected_result",
    [
        (["hello", "world", "apple", "pear", "banana", "pop"], ["pop"]),
        (["madam", "noon", "level", ""], ["madam", "noon", "level", ""]),
        ([], []),
    ],
)
def test_search_anagram(list_: list[str], expected_result: list[str]) -> None:
    assert search_anagram(list_) == expected_result


@pytest.mark.parametrize(
    "list_, expected_result", [([2, 3, 5, 7, 11], 77), ([-5, -7, -9, -13], 35), ([1, 2], 2), ([4], 0)]
)
def test_return_max_composition(list_: list[int], expected_result: int) -> None:
    assert return_max_composition(list_) == expected_result
