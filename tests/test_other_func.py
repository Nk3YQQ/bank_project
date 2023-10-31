import pytest

from src.other_func import calculate_area, check_email, count_number_in_list, sum_divisible_by_3_or_5


@pytest.mark.parametrize(
    "list_of_counts, expected_result", [([3, 5, 6, 10], 24), ([2, 3, 15, 20], 38), ([2, 4, 8, 11], 0), ([], 0)]
)
def test_sum_divisible_by_3_or_5(list_of_counts: list[int], expected_result: int) -> None:
    assert sum_divisible_by_3_or_5(list_of_counts) == expected_result


def test_check_email_with_valid_email() -> None:
    assert check_email("genrywilson@gmail.com") is True
    assert check_email("nikita.vasiliev@mail.ru") is True
    assert check_email("armen_ginaev@list.ru") is True
    assert check_email("andrey.bogdanov@yandex.ru") is True


def test_check_email_with_invalid_email() -> None:
    assert check_email("genrywilson@gmailcom") is False
    assert check_email("nikita.vasiliev") is False
    assert check_email("armen_ginaev@listru") is False


def test_check_email_with_empty_email() -> None:
    assert check_email("") is False


@pytest.fixture
def list_of_numbers() -> list[int]:
    return [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5]


def test_count_number_in_list(list_of_numbers: list[int]) -> None:
    assert count_number_in_list(list_of_numbers, 1) == 2
    assert count_number_in_list(list_of_numbers, 2) == 3
    assert count_number_in_list(list_of_numbers, 3) == 1
    assert count_number_in_list(list_of_numbers, 4) == 4
    assert count_number_in_list([], 3) == 0


@pytest.mark.parametrize(
    "shape, sides, expected_result",
    [
        ("треугольник", [8, 6, 5], 15),
        ("круг", [2], 13),
        ("прямоугольник", [4, 2, 4, 2], 8),
        ("квадрат", [], 0),
        ("кракозябра", [10, 7], None),
    ],
)
def test_calculate_area(shape: str, sides: list[int], expected_result: int | None) -> None:
    assert calculate_area(shape, sides) == expected_result
