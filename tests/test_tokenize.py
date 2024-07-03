from pytest import raises

# from calculator.tokenize import Tokenizer, remove_spaces, tokenize
from calculator.another_tokenize import tokenize


def test_tokenize():
  assert list(tokenize("")) == []
  assert list(tokenize("1 + 2")) == [1, "+", 2]
  assert list(tokenize("      1     -   8")) == [1, "-", 8]
  assert list(
      tokenize("0.34 * (7.1 - 5.9)")) == [0.34, "*", "(", 7.1, "-", 5.9, ")"]
  assert list(tokenize("-18 / 5 / 6")) == ["-", 18, "/", 5, "/", 6]

  with raises(ValueError):
    list(tokenize("100$ = 10000¢"))

  with raises(ValueError):
    list(tokenize("3.14.657 + 14"))


def test_remove_spaces():
  assert remove_spaces("1 + 2") == "1+2"
  assert remove_spaces("") == ""
  assert remove_spaces("  ") == ""


def test_read_number():
  assert Tokenizer("123").read_number() == 123
  assert Tokenizer("0").read_number() == 0
  assert Tokenizer("3.14").read_number() == 3.14
  assert Tokenizer("0+3").read_number() == 0
  assert Tokenizer("15.16*8").read_number() == 15.16
  assert Tokenizer(".").read_number() is None
  assert Tokenizer(".1+2").read_number() is None
  assert Tokenizer("###").read_number() is None


def test_tokenize():
    assert list(tokenize("")) == []
    assert list(tokenize("1 + 2")) == [1, "+", 2]
    assert list(tokenize("      1     -   8")) == [1, "-", 8]
    assert list(
        tokenize("0.34 * (7.1 - 5.9)")) == [0.34, "*", "(", 7.1, "-", 5.9, ")"]
    assert list(tokenize("-18 / 5 / 6")) == ["-", 18, "/", 5, "/", 6]
    with raises(ValueError):
        list(tokenize("100$ = 10000¢"))

    with raises(ValueError):
        list(tokenize("3.14.657 + 14"))