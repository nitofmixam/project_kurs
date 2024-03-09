from utils import filter_invalid_values, displayed_operations, load_file, displayed_sorted_operations
import pytest
import datetime


def test_filter_invalid_values():
    assert filter_invalid_values([1, None, {}, [], "hello", 5]) == [1, "hello", 5]
    assert filter_invalid_values([None, [], {}, 10, "world"]) == [10, "world"]
    assert filter_invalid_values([[], None, {}, []]) == []
    assert filter_invalid_values([]) == []
    assert filter_invalid_values([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_displayed_operations():
    filtered_items = [
        {'state': 'EXECUTED', 'date': '2021-01-01'},
        {'state': 'PENDING', 'date': '2021-01-02'},
        {'state': 'EXECUTED', 'date': '2021-01-03'},
    ]
    result = displayed_operations(filtered_items)
    assert len(result) <= 2


# Тест для функции load_file
def test_load_file():
    loaded_data = load_file()
    assert isinstance(loaded_data, list)


def test_displayed_sorted_operations(capsys):
    display_operations = [
        {
            'date': '2022-09-15T08:00:00.000',
            'description': 'Payment',
            'from': '1234567890123456',
            'to': '9876543210',
            'operationAmount': {
                'amount': 100.0,
                'currency': {'name': 'USD'}
            }
        }
    ]

    displayed_sorted_operations(display_operations)

    captured = capsys.readouterr()
    assert "15.09.2022 Payment" in captured.out
    assert "3456 -> *** 3210" in captured.out
    assert "100.0 USD" in captured.out


if __name__ == "__main__":
    pytest.main()
