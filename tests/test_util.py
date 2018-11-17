# coding: utf8
from __future__ import unicode_literals, print_function

import pytest
from wasabi.util import color, wrap, locale_escape


def test_color():
    assert color('test', fg='green') == '\x1b[38;5;2mtest\x1b[0m'
    assert color('test', fg=4) == '\x1b[38;5;4mtest\x1b[0m'
    assert color('test', bold=True) == '\x1b[1mtest\x1b[0m'
    assert color('test', fg=7, bg='red', bold=True) == '\x1b[1;38;5;7;48;5;1mtest\x1b[0m'


def test_wrap():
    text = "Hello world, this is a test."
    assert wrap(text, indent=0) == text
    assert wrap(text, indent=4) == "    Hello world, this is a test."
    assert wrap(text, wrap_max=10, indent=0) == "Hello\nworld,\nthis is a\ntest."
    assert wrap(text, wrap_max=5, indent=2) == "  Hello\n  world,\n  this\n  is\n  a\n  test."


@pytest.mark.parametrize('text', ['abc', '\u2713 abc', '👻'])
def test_locale_escape(text):
    assert locale_escape(text)
