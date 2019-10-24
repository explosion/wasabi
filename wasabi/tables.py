# coding: utf8
from __future__ import unicode_literals, print_function

from .util import to_string, zip_longest, basestring_


ALIGN_MAP = {"l": "<", "r": ">", "c": "^"}


def table(
    data,
    header=None,
    footer=None,
    divider=False,
    widths="auto",
    max_col=30,
    spacing=3,
    aligns=None,
    multiline=False,
):
    """Format tabular data.

    data (iterable / dict): The data to render. Either a list of lists (one per
        row) or a dict for two-column tables.
    header (iterable): The header columns.
    footer (iterable): The footer columns.
    divider (bool): Show a divider line between header/footer and body.
    widths (iterable or 'auto'): Column widths in order. If "auto", widths
        will be calculated automatically based on the largest value.
    max_col (int): Maximum column width.
    spacing (int): Spacing between columns, in spaces.
    aligns (iterable / unicode): Column alignments in order. 'l' (left,
        default), 'r' (right) or 'c' (center). If a string, value is used
        for all columns.
    multiline (bool): If a cell value is a list of a tuple, render it on
        multiple lines, with one value per line.
    RETURNS (unicode): The formatted table.
    """
    if isinstance(data, dict):
        data = list(data.items())
    if multiline:
        zipped_data = []
        for i, item in enumerate(data):
            vals = [v if isinstance(v, (list, tuple)) else [v] for v in item]
            zipped_data.extend(list(zip_longest(*vals, fillvalue="")))
            if i < len(data) - 1:
                zipped_data.append(["" for i in item])
        data = zipped_data
    if widths == "auto":
        widths = _get_max_widths(data, header, footer, max_col)
    settings = {"widths": widths, "spacing": spacing, "aligns": aligns}
    divider_row = row(["-" * width for width in widths], **settings)
    rows = []
    if header:
        rows.append(row(header, **settings))
        if divider:
            rows.append(divider_row)
    for i, item in enumerate(data):
        rows.append(row(item, **settings))
    if footer:
        if divider:
            rows.append(divider_row)
        rows.append(row(footer, **settings))
    return "\n{}\n".format("\n".join(rows))


def row(data, widths="auto", spacing=3, aligns=None):
    """Format data as a table row.

    data (iterable): The individual columns to format.
    widths (iterable, int or 'auto'): Column widths, either one integer for all
        columns or an iterable of values. If "auto", widths will be calculated
        automatically based on the largest value.
    spacing (int): Spacing between columns, in spaces.
    aligns (iterable / unicode): Column alignments in order. 'l' (left,
        default), 'r' (right) or 'c' (center). If a string, value is used
        for all columns.
    RETURNS (unicode): The formatted row.
    """
    cols = []
    if isinstance(aligns, basestring_):  # single align value
        aligns = [aligns for _ in data]
    if not hasattr(widths, "__iter__"):  # single number
        widths = [widths for _ in range(len(data))]
    for i, col in enumerate(data):
        align = ALIGN_MAP.get(aligns[i] if aligns and i < len(aligns) else "l")
        col_width = len(col) if widths == "auto" else widths[i]
        tpl = "{:%s%d}" % (align, col_width)
        cols.append(tpl.format(to_string(col)))
    return (" " * spacing).join(cols)


def _get_max_widths(data, header, footer, max_col):
    all_data = list(data)
    if header:
        all_data.append(header)
    if footer:
        all_data.append(footer)
    widths = [[len(to_string(col)) for col in item] for item in all_data]
    return [min(max(w), max_col) for w in list(zip(*widths))]
