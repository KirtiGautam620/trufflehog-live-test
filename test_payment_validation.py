from payment_validation import is_valid_amount


def test_positive_amount_is_valid():
    assert is_valid_amount(100)


def test_zero_amount_is_invalid():
    assert not is_valid_amount(0)
