import utils


def test_filter_invalid_values():
    assert utils.filter_invalid_values([1, None, {}, [], "hello", 5]) == [1, "hello", 5]
    assert utils.filter_invalid_values([None, [], {}, 10, "world"]) == [10, "world"]
    assert utils.filter_invalid_values([[], None, {}, []]) == []
    assert utils.filter_invalid_values([]) == []
    assert utils.filter_invalid_values([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
