# coding: utf8
from __future__ import unicode_literals, print_function

import os
import pytest
from wasabi.tables import table, row


@pytest.fixture()
def data():
    return [("Hello", "World", "12344342"), ("This is a test", "World", "1234")]


@pytest.fixture()
def header():
    return ["COL A", "COL B", "COL 3"]


@pytest.fixture()
def footer():
    return ["", "", "2030203.00"]


@pytest.fixture()
def fg_colors():
    return ["", "yellow", "87"]


@pytest.fixture()
def bg_colors():
    return ["green", "23", ""]


@pytest.fixture()
def color_values():
    return {"red": 76}


def test_table_default(data):
    result = table(data)
    assert (
        result
        == "\nHello            World   12344342\nThis is a test   World   1234    \n"
    )


def test_table_header(data, header):
    result = table(data, header=header)
    assert (
        result
        == "\nCOL A            COL B   COL 3   \nHello            World   12344342\nThis is a test   World   1234    \n"
    )


def test_table_header_footer_divider(data, header, footer):
    result = table(data, header=header, footer=footer, divider=True)
    assert (
        result
        == "\nCOL A            COL B   COL 3     \n--------------   -----   ----------\nHello            World   12344342  \nThis is a test   World   1234      \n--------------   -----   ----------\n                         2030203.00\n"
    )


def test_table_aligns(data):
    result = table(data, aligns=("r", "c", "l"))
    assert (
        result
        == "\n         Hello   World   12344342\nThis is a test   World   1234    \n"
    )


def test_table_aligns_single(data):
    result = table(data, aligns="r")
    assert (
        result
        == "\n         Hello   World   12344342\nThis is a test   World       1234\n"
    )


def test_table_widths():
    data = [("a", "bb", "ccc"), ("d", "ee", "fff")]
    widths = (5, 2, 10)
    result = table(data, widths=widths)
    assert result == "\na       bb   ccc       \nd       ee   fff       \n"


def test_row_single_widths():
    data = ("a", "bb", "ccc")
    result = row(data, widths=10)
    assert result == "a            bb           ccc       "


def test_table_multiline(header):
    data = [
        ("hello", ["foo", "bar", "baz"], "world"),
        ("hello", "world", ["world 1", "world 2"]),
    ]
    result = table(data, header=header, divider=True, multiline=True)
    assert (
        result
        == "\nCOL A   COL B   COL 3  \n-----   -----   -------\nhello   foo     world  \n        bar            \n        baz            \n                       \nhello   world   world 1\n                world 2\n"
    )


def test_row_fg_colors(fg_colors):
    result = row(("Hello", "World", "12344342"), fg_colors=fg_colors)
    assert result == "Hello   \x1b[38;5;3mWorld\x1b[0m   \x1b[38;5;87m12344342\x1b[0m"


def test_row_bg_colors(bg_colors):
    result = row(("Hello", "World", "12344342"), bg_colors=bg_colors)
    assert result == "\x1b[48;5;2mHello\x1b[0m   \x1b[48;5;23mWorld\x1b[0m   12344342"


def test_row_fg_colors_and_bg_colors(fg_colors, bg_colors):
    result = row(
        ("Hello", "World", "12344342"), fg_colors=fg_colors, bg_colors=bg_colors
    )
    assert (
        result
        == "\x1b[48;5;2mHello\x1b[0m   \x1b[38;5;3;48;5;23mWorld\x1b[0m   \x1b[38;5;87m12344342\x1b[0m"
    )


def test_colors_whole_table_with_automatic_widths(
    data, header, footer, fg_colors, bg_colors
):
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
    )
    assert (
        result
        == "\n\x1b[48;5;2mCOL A         \x1b[0m   \x1b[38;5;3;48;5;23mCOL B\x1b[0m   \x1b[38;5;87mCOL 3     \x1b[0m\n\x1b[48;5;2m--------------\x1b[0m   \x1b[38;5;3;48;5;23m-----\x1b[0m   \x1b[38;5;87m----------\x1b[0m\n\x1b[48;5;2mHello         \x1b[0m   \x1b[38;5;3;48;5;23mWorld\x1b[0m   \x1b[38;5;87m12344342  \x1b[0m\n\x1b[48;5;2mThis is a test\x1b[0m   \x1b[38;5;3;48;5;23mWorld\x1b[0m   \x1b[38;5;87m1234      \x1b[0m\n\x1b[48;5;2m--------------\x1b[0m   \x1b[38;5;3;48;5;23m-----\x1b[0m   \x1b[38;5;87m----------\x1b[0m\n\x1b[48;5;2m              \x1b[0m   \x1b[38;5;3;48;5;23m     \x1b[0m   \x1b[38;5;87m2030203.00\x1b[0m\n"
    )


def test_colors_whole_table_only_fg_colors(data, header, footer, fg_colors):
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
    )
    assert result


def test_colors_whole_table_only_bg_colors(data, header, footer, bg_colors):
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        bg_colors=bg_colors,
    )
    assert result


def test_colors_whole_table_with_supplied_spacing(
    data, header, footer, fg_colors, bg_colors
):
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
        spacing=5,
    )
    assert result


def test_colors_whole_table_with_supplied_widths(
    data, header, footer, fg_colors, bg_colors
):
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
        widths=(5, 2, 10),
    )
    assert result


def test_colors_whole_table_with_single_alignment(
    data, header, footer, fg_colors, bg_colors
):
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
        aligns="r",
    )
    assert result


def test_colors_whole_table_with_multiple_alignment(
    data, header, footer, fg_colors, bg_colors
):
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
        aligns=("c", "r", "l"),
    )
    assert result


def test_colors_whole_table_with_multiline(data, header, footer, fg_colors, bg_colors):
    result = table(
        data=((["Charles", "Quinton", "Murphy"], "my", "brother"), ("1", "2", "3")),
        fg_colors=fg_colors,
        bg_colors=bg_colors,
        multiline=True,
    )
    assert result


def test_colors_whole_table_log_friendly(data, header, footer, fg_colors, bg_colors):
    ENV_LOG_FRIENDLY = "WASABI_LOG_FRIENDLY"
    os.environ[ENV_LOG_FRIENDLY] = "True"
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
    )
    assert (
        result
        == "\nCOL A            COL B   COL 3     \n--------------   -----   ----------\nHello            World   12344342  \nThis is a test   World   1234      \n--------------   -----   ----------\n                         2030203.00\n"
    )
    del os.environ[ENV_LOG_FRIENDLY]


def test_colors_whole_table_log_friendly_prefix(
    data, header, footer, fg_colors, bg_colors
):
    ENV_LOG_FRIENDLY = "CUSTOM_LOG_FRIENDLY"
    os.environ[ENV_LOG_FRIENDLY] = "True"
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
        env_prefix="CUSTOM",
    )
    assert (
        result
        == "\nCOL A            COL B   COL 3     \n--------------   -----   ----------\nHello            World   12344342  \nThis is a test   World   1234      \n--------------   -----   ----------\n                         2030203.00\n"
    )
    del os.environ[ENV_LOG_FRIENDLY]


def test_colors_whole_table_supports_ansi_false(
    data, header, footer, fg_colors, bg_colors
):
    os.environ["ANSI_COLORS_DISABLED"] = "True"
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
    )
    assert (
        result
        == "\nCOL A            COL B   COL 3     \n--------------   -----   ----------\nHello            World   12344342  \nThis is a test   World   1234      \n--------------   -----   ----------\n                         2030203.00\n"
    )
    del os.environ["ANSI_COLORS_DISABLED"]


def test_colors_whole_table_color_values(data, header, footer, fg_colors, bg_colors):
    result = table(
        data,
        header=header,
        footer=footer,
        divider=True,
        fg_colors=fg_colors,
        bg_colors=bg_colors,
        color_values={"yellow": 11},
    )
    assert result
