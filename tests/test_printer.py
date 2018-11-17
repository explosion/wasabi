# coding: utf8
from __future__ import unicode_literals, print_function

import pytest
from wasabi.printer import Printer
from wasabi.util import MESSAGES


def test_printer():
    p = Printer(no_print=True)
    text = "This is a test."
    assert p.good(text) == "\x1b[38;5;2m\u2713 This is a test.\x1b[0m"
    assert p.fail(text) == "\x1b[38;5;1m\u2718 This is a test.\x1b[0m"
    assert p.warn(text) == "\x1b[38;5;3m\u26a0 This is a test.\x1b[0m"
    assert p.info(text) == "\x1b[38;5;4m\u2139 This is a test.\x1b[0m"
    assert p.text(text) == text


def test_printer_no_pretty():
    p = Printer(no_print=True, pretty=False)
    text = "This is a test."
    assert p.good(text) == text
    assert p.fail(text) == text
    assert p.warn(text) == text
    assert p.info(text) == text
    assert p.text(text) == text


def test_printer_custom():
    colors = {'yellow': 220, 'purple': 99}
    icons = {'warn': '\u26a0\ufe0f', 'question': "?"}
    p = Printer(no_print=True, colors=colors, icons=icons)
    text = "This is a test."
    assert p.text(text, color='purple', icon='question') == "\x1b[38;5;99m? This is a test.\x1b[0m"
    assert p.warn(text) == "\x1b[38;5;3m\u26a0\ufe0f This is a test.\x1b[0m"


def test_printer_counts():
    p = Printer()
    text = "This is a test."
    for i in range(2):
        p.good(text)
    for i in range(1):
        p.fail(text)
    for i in range(4):
        p.warn(text)
    assert p.counts[MESSAGES.GOOD] == 2
    assert p.counts[MESSAGES.FAIL] == 1
    assert p.counts[MESSAGES.WARN] == 4


def test_printer_divider():
    p = Printer(line_max=20, no_print=True)
    p.divider() == "\x1b[1m\n================\x1b[0m"
    p.divider('test') == "\x1b[1m\n====== test ======\x1b[0m"
    p.divider('test', char='*') == "\x1b[1m\n****** test ******\x1b[0m"
    p.divider('This is a very long text, it is very long') == "\x1b[1m\n This is a very long text, it is very long \x1b[0m"
    with pytest.raises(ValueError):
        p.divider('test', char='~.')
