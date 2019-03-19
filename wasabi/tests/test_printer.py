# coding: utf8
from __future__ import unicode_literals, print_function

import pytest
import time
import os
from wasabi.printer import Printer
from wasabi.util import MESSAGES, supports_ansi


def test_printer():
    p = Printer(no_print=True)
    text = "This is a test."
    if supports_ansi():
        assert p.good(text) in (
            "\x1b[38;5;2m\u2714 This is a test.\x1b[0m",
            "\x1b[38;5;2mThis is a test.\x1b[0m",
        )
        assert p.fail(text) in (
            "\x1b[38;5;1m\u2718 This is a test.\x1b[0m",
            "\x1b[38;5;1mThis is a test.\x1b[0m",
        )
        assert p.warn(text) in (
            "\x1b[38;5;3m\u26a0 This is a test.\x1b[0m",
            "\x1b[38;5;3mThis is a test.\x1b[0m",
        )
        assert p.info(text) in (
            "\x1b[38;5;4m\u2139 This is a test.\x1b[0m",
            "\x1b[38;5;4mThis is a test.\x1b[0m",
        )
        assert p.text(text) == text
    else:
        assert p.good(text) in (text, "\u2714 This is a test.")
        assert p.fail(text) in (text, "\u2718 This is a test.")
        assert p.warn(text) in (text, "\u26a0 This is a test.")
        assert p.info(text) in (text, "\u2139 This is a test.")
        assert p.text(text) == text


def test_printer_print():
    p = Printer()
    text = "This is a test."
    p.good(text)
    p.fail(text)
    p.info(text)
    p.text(text)


def test_printer_no_pretty():
    p = Printer(no_print=True, pretty=False)
    text = "This is a test."
    assert p.good(text) == text
    assert p.fail(text) == text
    assert p.warn(text) == text
    assert p.info(text) == text
    assert p.text(text) == text


def test_printer_custom():
    colors = {"yellow": 220, "purple": 99}
    icons = {"warn": "\u26a0\ufe0f", "question": "?"}
    p = Printer(no_print=True, colors=colors, icons=icons)
    text = "This is a test."
    purple_question = p.text(text, color="purple", icon="question")
    warning = p.warn(text)
    assert purple_question in (
        "\x1b[38;5;99m? This is a test.\x1b[0m",
        "{} {}".format(icons["question"], text),
    )
    assert warning in (
        "\x1b[38;5;3m\u26a0\ufe0f This is a test.\x1b[0m",
        "\x1b[38;5;3mThis is a test.\x1b[0m",
        "\u26a0\ufe0f This is a test.",
        text,
    )


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
    p.divider("test") == "\x1b[1m\n====== test ======\x1b[0m"
    p.divider("test", char="*") == "\x1b[1m\n****** test ******\x1b[0m"
    assert (
        p.divider("This is a very long text, it is very long")
        == "\x1b[1m\n This is a very long text, it is very long \x1b[0m"
    )
    with pytest.raises(ValueError):
        p.divider("test", char="~.")


@pytest.mark.parametrize("hide_animation", [False, True])
def test_printer_loading(hide_animation):
    p = Printer(hide_animation=hide_animation)
    print("\n")
    with p.loading("Loading..."):
        time.sleep(1)
    p.good("Success!")

    with p.loading("Something else..."):
        time.sleep(2)
    p.good("Yo!")

    with p.loading("Loading..."):
        time.sleep(1)
    p.good("Success!")


def test_printer_loading_raises_exception():
    def loading_with_exception():
        p = Printer()
        print("\n")
        with p.loading():
            raise Exception("This is an error.")

    with pytest.raises(Exception):
        loading_with_exception()


def test_printer_log_friendly():
    text = "This is a test."
    ENV_LOG_FRIENDLY = "WASABI_LOG_FRIENDLY"
    os.environ[ENV_LOG_FRIENDLY] = "True"
    p = Printer(no_print=True)
    assert p.good(text) in ("\u2714 This is a test.", text)
    del os.environ[ENV_LOG_FRIENDLY]


def test_printer_log_friendly_prefix():
    text = "This is a test."
    ENV_LOG_FRIENDLY = "CUSTOM_LOG_FRIENDLY"
    os.environ[ENV_LOG_FRIENDLY] = "True"
    p = Printer(no_print=True, env_prefix="CUSTOM")
    assert p.good(text) in (text, "\u2714 This is a test.")
    print(p.good(text))
    del os.environ[ENV_LOG_FRIENDLY]


def test_printer_none_encoding(monkeypatch):
    """Test that printer works even if sys.stdout.encoding is set to None. This
    previously caused a very confusing error."""
    monkeypatch.setattr("sys.stdout.encoding", None)
    p = Printer()
