from typing import Any

import pytest

from src.utils import get_transaction_on_rub, get_transactions

transactions = get_transactions()


@pytest.fixture
def data() -> list[dict]:
    transaction_list = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472",
        },
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        },
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472",
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {"amount": "77751.04", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493",
        },
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-26T15:40:13.413061",
            "operationAmount": {"amount": "50870.71", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 43597928997568165086",
        },
    ]
    return transaction_list


def test_get_transactions(data: dict) -> None:
    assert isinstance(transactions, list)
    assert transactions[0] == data[0]
    assert transactions[8] == data[4]
    assert transactions[12] == data[8]
    assert get_transactions("../data/hole.json") == []


@pytest.mark.parametrize(
    "transaction, expected_result",
    [
        (transactions[0], 31957.58),
        (transactions[6], ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")),
        (transactions[7], ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")),
        (transactions[9], 79931.03),
        (transactions[10], ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")),
        (transactions[13], 77751.04),
    ],
)
def test_get_transaction_on_rub(transaction: dict[Any, Any], expected_result: float | ValueError) -> None:
    if isinstance(expected_result, ValueError):
        with pytest.raises(ValueError):
            get_transaction_on_rub(transaction)
    else:
        assert get_transaction_on_rub(transaction) == expected_result
