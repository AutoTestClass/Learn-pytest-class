import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def second_entry():
    return 2


# Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]


# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string_1(order, expected_list):
    # Act
    order.append(3.0)
    # Assert
    assert order == expected_list


def test_string_2(order, expected_list):
    # Act
    order.append(4.0)
    # Assert
    assert order == expected_list
