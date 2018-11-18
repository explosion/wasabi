# coding: utf8
from __future__ import unicode_literals, print_function

from .util import to_string


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
    aligns (iterable): Column alignments in order. 'l' (left, default), 'r'
        (right) or 'c' (center).
    RETURNS (unicode): The formatted table.
    """
    if isinstance(data, dict):
        data = list(data.items())
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
    widths (iterable or 'auto'): Column widths in order. If "auto", widths
        will be calculated automatically based on the largest value.
    spacing (int): Spacing between columns, in spaces.
    aligns (iterable): Column alignments in order. 'l' (left, default), 'r'
        (right) or 'c' (center).
    RETURNS (unicode): The formatted row.
    """
    cols = []
    for i, col in enumerate(data):
        align = ALIGN_MAP.get(aligns[i] if aligns else "l")
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
