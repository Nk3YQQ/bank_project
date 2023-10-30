import pytest

from src.processing import avg_cost_and_quantity, get_list_with_state, sort_list_by_date, sort_list_by_price


@pytest.fixture
def coll() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def info_about_products() -> list[dict]:
    return [
        {"name": "apple", "price": 40, "category": "fruits", "quantity": 14},
        {"name": "potato", "price": 20, "category": "vegetables", "quantity": 30},
        {"name": "banana", "price": 120, "category": "fruits", "quantity": 8},
        {"name": "tomato", "price": 60, "category": "vegetables", "quantity": 12},
        {"name": "chicken", "price": 260, "category": "meat", "quantity": 3},
        {"name": "pork", "price": 150, "category": "meat", "quantity": 5},
    ]


@pytest.fixture
def info_about_internet_orders() -> list[dict]:
    return [
        {"id": 1, "date": "2023-09-15", "items": [{"name": "Table", "price": 8000, "quantity": 1}]},
        {"id": 2, "date": "2023-09-26", "items": [{"name": "Notebooks", "price": 300, "quantity": 12}]},
        {"id": 3, "date": "2023-10-04", "items": [{"name": "TV", "price": 20000, "quantity": 1}]},
        {"id": 4, "date": "2023-10-19", "items": [{"name": "Milk", "price": 600, "quantity": 10}]},
        {"id": 5, "date": "2023-11-01", "items": [{"name": "T-shirts", "price": 2000, "quantity": 5}]},
        {"id": 6, "date": "2023-11-05", "items": [{"name": "Sneakers", "price": 6000, "quantity": 1}]},
    ]


def test_get_list_with_state(coll: list[dict]) -> None:
    assert get_list_with_state(coll) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert get_list_with_state(coll, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert get_list_with_state([]) == []


def test_sort_list_by_date(list_of_date: list[dict]) -> None:
    assert sort_list_by_date(list_of_date, True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_list_by_date(list_of_date) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sort_list_by_date([]) == []


def test_sort_list_by_price(info_about_products: list[dict]) -> None:
    assert sort_list_by_price(info_about_products) == [
        {"name": "chicken", "price": 260, "category": "meat", "quantity": 3},
        {"name": "pork", "price": 150, "category": "meat", "quantity": 5},
        {"name": "banana", "price": 120, "category": "fruits", "quantity": 8},
        {"name": "tomato", "price": 60, "category": "vegetables", "quantity": 12},
        {"name": "apple", "price": 40, "category": "fruits", "quantity": 14},
        {"name": "potato", "price": 20, "category": "vegetables", "quantity": 30},
    ]
    assert sort_list_by_price(info_about_products, "meat") == [
        {"name": "chicken", "price": 260, "category": "meat", "quantity": 3},
        {"name": "pork", "price": 150, "category": "meat", "quantity": 5},
    ]
    assert sort_list_by_price(info_about_products, "fruits") == [
        {"name": "banana", "price": 120, "category": "fruits", "quantity": 8},
        {"name": "apple", "price": 40, "category": "fruits", "quantity": 14},
    ]
    assert sort_list_by_price(info_about_products, "vegetables") == [
        {"name": "tomato", "price": 60, "category": "vegetables", "quantity": 12},
        {"name": "potato", "price": 20, "category": "vegetables", "quantity": 30},
    ]
    assert sort_list_by_price([]) == []


def test_avg_cost_and_quantity(info_about_internet_orders: list[dict]) -> None:
    assert avg_cost_and_quantity(info_about_internet_orders) == {
        "2023-09": {"average_order_value": 4150.0, "order_count": 2},
        "2023-10": {"average_order_value": 10300.0, "order_count": 2},
        "2023-11": {"average_order_value": 4000.0, "order_count": 2},
    }
