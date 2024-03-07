from utils import filter_invalid_values, displayed_operations, displayed_sorted_operations


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
    assert len(result) <= 5


def test_displayed_sorted_operations():
    display_operations = [
        {
            'date': '2022-01-01T12:00:00.000',
            'description': 'Payment',
            'from': '1234567890123456',
            'to': '9876543210',
            'operationAmount': {
                'amount': 100,
                'currency': {'name': 'USD'}
            }
        }
    ]
    displayed_sorted_operations(display_operations)