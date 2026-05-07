import pytest
from compound_interest import compound_interest


def test_basic_annual_compounding():
    amount, interest = compound_interest(1000, 5, 3, 1)
    assert amount == 1157.63
    assert interest == 157.63


def test_monthly_compounding():
    amount, interest = compound_interest(1000, 5, 3, 12)
    assert amount == 1161.47
    assert interest == 161.47


def test_daily_compounding():
    amount, interest = compound_interest(1000, 5, 1, 365)
    assert amount == 1051.27
    assert interest == 51.27


def test_zero_interest_rate():
    amount, interest = compound_interest(1000, 0, 5, 12)
    assert amount == 1000.0
    assert interest == 0.0


def test_zero_time():
    amount, interest = compound_interest(1000, 5, 0, 12)
    assert amount == 1000.0
    assert interest == 0.0


def test_large_principal():
    amount, interest = compound_interest(100000, 8, 10, 4)
    assert amount == 220803.97
    assert interest == 120803.97


def test_returns_tuple():
    result = compound_interest(500, 10, 2, 1)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_interest_always_non_negative():
    _, interest = compound_interest(500, 5, 2, 12)
    assert interest >= 0


def test_amount_greater_than_principal_with_positive_rate():
    amount, _ = compound_interest(1000, 5, 1, 1)
    assert amount > 1000
