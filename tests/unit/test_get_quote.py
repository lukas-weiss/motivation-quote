import pytest

from motivation_quote import app

def test_get_quote():
    result = app.get_quote("tests/unit/data/quotes.csv")
    assert result is not None
    assert result[0] is not None
    assert len(result[0]) > 0
    assert result[1] is not None
    assert len(result[1]) > 0

def test_get_no_quote():
    result = app.get_quote("tests/unit/quotes2.csv")
    assert result is None

def test_get_first_quote():
    result = app.get_quote("tests/unit/data/single_quotes.csv")
    assert result is not None
    assert result[0] is not None
    assert len(result[0]) > 0
    assert result[1] is not None
    assert len(result[1]) > 0
    print(result[0])
    print(result[1])
    assert result[0] == "Build not born"
    assert result[1] == "Arnold Schwarzenegger"

