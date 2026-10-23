import pytest

from api_parity.comparator import Difference, compare_json


def test_matching_values():
    assert compare_json("hello", "hello") == []


def test_different_values():
    result = compare_json("hello", "world")

    assert result == [
        Difference(
            path="$",
            expected="hello",
            actual="world",
        )
    ]


def test_object_key_order_does_not_matter():
    expected = {"id": 1, "name": "Alice"}
    actual = {"name": "Alice", "id": 1}

    assert compare_json(expected, actual) == []


def test_nested_object_reports_field_path():
    expected = {
        "user": {
            "id": 1,
            "active": True,
        }
    }

    actual = {
        "user": {
            "id": 1,
            "active": False,
        }
    }

    result = compare_json(expected, actual)

    assert result == [
        Difference(
            path="$.user.active",
            expected=True,
            actual=False,
        )
    ]


@pytest.mark.parametrize(
    "expected, actual",
    [
        ("hello", {"message": "hello"}),
        ([1, 2], {"items": [1, 2]}),
        ([1, 2], "hello"),
        (None, []),
        (True, 1),
        (False, 0),
    ],
)
def test_different_json_types(expected, actual):
    result = compare_json(expected, actual)

    assert result == [
        Difference(
            path="$",
            expected=expected,
            actual=actual,
        )
    ]


def test_list_element_difference():
    expected = [10, 20, 30]
    actual = [10, 99, 30]

    result = compare_json(expected, actual)

    assert result == [
        Difference(
            path="$[1]",
            expected=20,
            actual=99,
        )
    ]


def test_nested_list_difference():
    expected = {
        "users": [
            {"name": "Alice"},
            {"name": "Bob"},
        ]
    }

    actual = {
        "users": [
            {"name": "Alice"},
            {"name": "John"},
        ]
    }

    result = compare_json(expected, actual)

    assert result == [
        Difference(
            path="$.users[1].name",
            expected="Bob",
            actual="John",
        )
    ]
