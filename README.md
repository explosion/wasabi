# wasabi: A lightweight console printing and formatting toolkit

Over the years, I've written countless implementations of coloring and
formatting utilities to output messages in our libraries like
[spaCy](https://spacy.io), [Thinc](https://github.com/explosion/thinc) and
[Prodigy](https://prodi.gy). While there are many other great open-source
options, I've always ended up wanting something slightly different or slightly
custom.

This package is still a work in progress and aims to bundle those utilities in a
standardised way so they can be shared across our other projects. It's super
lightweight, has zero dependencies and works with Python 3.6+.

[![Azure Pipelines](https://img.shields.io/azure-devops/build/explosion-ai/public/1/master.svg?logo=azure-pipelines&style=flat-square)](https://dev.azure.com/explosion-ai/public/_build?definitionId=1)
[![PyPi](https://img.shields.io/pypi/v/wasabi.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.python.org/pypi/wasabi)
[![conda](https://img.shields.io/conda/vn/conda-forge/wasabi.svg?style=flat-square&logo=conda-forge/logoColor=white)](https://anaconda.org/conda-forge/wasabi)
[![GitHub](https://img.shields.io/github/release/ines/wasabi/all.svg?style=flat-square&logo=github)](https://github.com/ines/wasabi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

<img width="609" src="https://user-images.githubusercontent.com/13643239/48663861-8c9ea000-ea96-11e8-8b04-d120c52276a8.png">

## 💬 FAQ

### Are you going to add more features?

Yes, there's still a few of helpers and features to port over. However, the new
features will be heavily biased by what we (think we) need. I always appreciate
pull requests to improve the existing functionality – but I want to keep this
library as simple, lightweight and specific as possible.

### Can I use this for my projects?

Sure, if you like it, feel free to adopt it! Just keep in mind that the package
is very specific and not intended to be a full-featured and fully customisable
formatting library. If that's what you're looking for, you might want to try
other packages – for example, [`colored`](https://pypi.org/project/colored/),
[`crayons`](https://github.com/kennethreitz/crayons),
[`colorful`](https://github.com/timofurrer/colorful),
[`tabulate`](https://bitbucket.org/astanin/python-tabulate),
[`console`](https://github.com/mixmastamyk/console) or
[`py-term`](https://github.com/gravmatt/py-term), to name a few.

### Why `wasabi`?

I was looking for a short and descriptive name, but everything was already
taken. So I ended up naming this package after one of my rats, Wasabi. 🐀

## ⌛️ Installation

```bash
pip install wasabi
```

## 🎛 API

### <kbd>function</kbd> `msg`

An instance of `Printer`, initialized with the default config. Useful as a quick
shortcut if you don't need to customize initialization.

```python
from wasabi import msg

msg.good("Success!")
```

### <kbd>class</kbd> `Printer`

#### <kbd>method</kbd> `Printer.__init__`

```python
from wasabi import Printer

msg = Printer()
```

| Argument          | Type      | Description                                                   | Default       |
| ----------------- | --------- | ------------------------------------------------------------- | ------------- |
| `pretty`          | bool      | Pretty-print output with colors and icons.                    | `True`        |
| `no_print`        | bool      | Don't actually print, just return.                            | `False`       |
| `colors`          | dict      | Add or overwrite color values, names mapped to `0`-`256`.     | `None`        |
| `icons`           | dict      | Add or overwrite icon. Name mapped to unicode.                | `None`        |
| `line_max`        | int       | Maximum line length (for divider).                            | `80`          |
| `animation`       | str       | Steps of loading animation for `Printer.loading`.             | `"⠙⠹⠸⠼⠴⠦⠧⠇⠏"` |
| `animation_ascii` | str       | Alternative animation for ASCII terminals.                    | `"\|/-\\"`    |
| `hide_animation`  | bool      | Don't display animation, e.g. for logs.                       | `False`       |
| `ignore_warnings` | bool      | Don't output messages of type `MESSAGE.WARN`.                 | `False`       |
| `env_prefix`      | str       | Prefix for environment variables, e.g. `WASABI_LOG_FRIENDLY`. | `"WASABI"`    |
| `timestamp`       | bool      | Add timestamp before output.                                  | `False`       |
| **RETURNS**       | `Printer` | The initialized printer.                                      | -             |

#### <kbd>method</kbd> `Printer.text`

```python
msg = Printer()
msg.text("Hello world!")
```

| Argument   | Type           | Description                                                                                                            | Default |
| ---------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ------- |
| `title`    | str            | The main text to print.                                                                                                | `""`    |
| `text`     | str            | Optional additional text to print.                                                                                     | `""`    |
| `color`    |  unicode / int | Color name or value.                                                                                                   | `None`  |
| `icon`     | str            | Name of icon to add.                                                                                                   | `None`  |
| `show`     | bool           | Whether to print or not. Can be used to only output messages under certain condition, e.g. if `--verbose` flag is set. | `True`  |
| `spaced`   | bool           | Whether to add newlines around the output.                                                                             | `False` |
| `no_print` | bool           | Don't actually print, just return. Overwrites global setting.                                                          | `False` |
| `exits`    | int            | If set, perform a system exit with the given code after printing.                                                      | `None`  |

#### <kbd>method</kbd> `Printer.good`, `Printer.fail`, `Printer.warn`, `Printer.info`

Print special formatted messages.

```python
msg = Printer()
msg.good("Success")
msg.fail("Error")
msg.warn("Warning")
msg.info("Info")
```

| Argument | Type | Description                                                                                                            | Default |
| -------- | ---- | ---------------------------------------------------------------------------------------------------------------------- | ------- |
| `title`  | str  | The main text to print.                                                                                                | `""`    |
| `text`   | str  | Optional additional text to print.                                                                                     | `""`    |
| `show`   | bool | Whether to print or not. Can be used to only output messages under certain condition, e.g. if `--verbose` flag is set. | `True`  |
| `exits`  | int  | If set, perform a system exit with the given code after printing.                                                      | `None`  |

#### <kbd>method</kbd> `Printer.divider`

Print a formatted divider.

```python
msg = Printer()
msg.divider("Heading")
```

| Argument | Type | Description                                                                                                            | Default |
| -------- | ---- | ---------------------------------------------------------------------------------------------------------------------- | ------- |
| `text`   | str  | Headline text. If empty, only the line is printed.                                                                     | `""`    |
| `char`   | str  | Single line character to repeat.                                                                                       | `"="`   |
| `show`   | bool | Whether to print or not. Can be used to only output messages under certain condition, e.g. if `--verbose` flag is set. | `True`  |
| `icon`   | str  | Optional icon to use with title.                                                                                       | `None`  |

#### <kbd>contextmanager</kbd> `Printer.loading`

```python
msg = Printer()
with msg.loading("Loading..."):
    # Do something here that takes longer
    time.sleep(10)
msg.good("Successfully loaded something!")
```

| Argument | Type | Description                        | Default           |
| -------- | ---- | ---------------------------------- | ----------------- |
| `text`   | str  | The text to display while loading. | `"Loading..."`    |

#### <kbd>method</kbd> `Printer.table`, `Printer.row`

See [Tables](#tables).

#### <kbd>property</kbd> `Printer.counts`

Get the counts of how often the special printers were fired, e.g.
`MESSAGES.GOOD`. Can be used to print an overview like "X warnings"

```python
msg = Printer()
msg.good("Success")
msg.fail("Error")
msg.warn("Error")

print(msg.counts)
# Counter({'good': 1, 'fail': 2, 'warn': 0, 'info': 0})
```

| Argument    | Type      | Description                                          |
| ----------- | --------- | ---------------------------------------------------- |
| **RETURNS** | `Counter` | The counts for the individual special message types. |

### Tables

#### <kbd>function</kbd> `table`

Lightweight helper to format tabular data.

```python
from wasabi import table

data = [("a1", "a2", "a3"), ("b1", "b2", "b3")]
header = ("Column 1", "Column 2", "Column 3")
widths = (8, 9, 10)
aligns = ("r", "c", "l")
formatted = table(data, header=header, divider=True, widths=widths, aligns=aligns)
```

```
Column 1   Column 2    Column 3
--------   ---------   ----------
      a1      a2       a3
      b1      b2       b3
```

| Argument    | Type                | Description                                                                                                                         | Default  |
| ----------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `data`      | iterable / dict     | The data to render. Either a list of lists (one per row) or a dict for two-column tables.                                           |          |
| `header`    | iterable            | Optional header columns.                                                                                                            | `None`   |
| `footer`    | iterable            | Optional footer columns.                                                                                                            | `None`   |
| `divider`   | bool                | Show a divider line between header/footer and body.                                                                                 | `False`  |
| `widths`    | iterable / `"auto"` | Column widths in order. If `"auto"`, widths will be calculated automatically based on the largest value.                            | `"auto"` |
| `max_col`   | int                 | Maximum column width.                                                                                                               | `30`     |
| `spacing`   | int                 | Number of spaces between columns.                                                                                                   | `3`      |
| `aligns`    | iterable / unicode  | Columns alignments in order. `"l"` (left, default), `"r"` (right) or `"c"` (center). If If a string, value is used for all columns. | `None`   |
| `multiline` | bool                | If a cell value is a list of a tuple, render it on multiple lines, with one value per line.                                         | `False`  |
| `env_prefix` | unicode                | Prefix for environment variables, e.g. WASABI_LOG_FRIENDLY.                                         | `"WASABI"` |
| `color_values` | dict                | Add or overwrite color values, name mapped to value.                                         | `None`   |
| `fg_colors` | iterable                | Foreground colors, one per column. None can be specified for individual columns to retain the default background color. | `None`   |
| `bg_colors` | iterable                | Background colors, one per column. None can be specified for individual columns to retain the default background color. | `None`   |
| **RETURNS** | str                 | The formatted table.                                                                                                                |          |

#### <kbd>function</kbd> `row`

```python
from wasabi import row

data = ("a1", "a2", "a3")
formatted = row(data)
```

```
a1   a2   a3
```

| Argument    | Type                      | Description                                                                                                                                                | Default  |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `data`      | iterable                  | The individual columns to format.                                                                                                                          |          |
| `widths`    | list / int / `"auto"` | Column widths, either one integer for all columns or an iterable of values. If "auto", widths will be calculated automatically based on the largest value. | `"auto"` |
| `spacing`   | int                       | Number of spaces between columns.                                                                                                                          | `3`      |
| `aligns`    | list                  | Columns alignments in order. `"l"` (left), `"r"` (right) or `"c"` (center).                                                                                | `None`   |
| `env_prefix` | unicode                | Prefix for environment variables, e.g. WASABI_LOG_FRIENDLY.                                         | `"WASABI"` |
| `fg_colors`    | list                  | Foreground colors for the columns, in order. None can be specified for individual columns to retain the default foreground color. | `None`   |
| `bg_colors`    | list                  | Background colors for the columns, in order. None can be specified for individual columns to retain the default background color. | `None`   |
| **RETURNS** | str                       | The formatted row.                                                                                                                                         |          |

### <kbd>class</kbd> `TracebackPrinter`

Helper to output custom formatted tracebacks and error messages. Currently used
in [Thinc](https://github.com/explosion/thinc).

#### <kbd>method</kbd> `TracebackPrinter.__init__`

Initialize a traceback printer.

```python
from wasabi import TracebackPrinter

tb = TracebackPrinter(tb_base="thinc", tb_exclude=("check.py",))
```

| Argument          | Type               | Description                                                                                                                                                              | Default    |
| ----------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `color_error`     | str / int          | Color name or code for errors (passed to `color` helper).                                                                                                                | `"red"`    |
| `color_tb`        | str / int          | Color name or code for traceback headline (passed to `color` helper).                                                                                                    | `"blue"`   |
| `color_highlight` | str / int          | Color name or code for highlighted text (passed to `color` helper).                                                                                                      | `"yellow"` |
| `indent`          | int                | Number of spaces to use for indentation.                                                                                                                                 | `2`        |
| `tb_base`         | str                | Name of directory to use to show relative paths. For example, `"thinc"` will look for the last occurence of `"/thinc/"` in a path and only show path to the right of it. | `None`     |
| `tb_exclude`      | tuple              | List of filenames to exclude from traceback.                                                                                                                             | `tuple()`  |
| **RETURNS**       | `TracebackPrinter` | The traceback printer.                                                                                                                                                   |            |

#### <kbd>method</kbd> `TracebackPrinter.__call__`

Output custom formatted tracebacks and errors.

```python
from wasabi import TracebackPrinter
import traceback

tb = TracebackPrinter(tb_base="thinc", tb_exclude=("check.py",))

error = tb("Some error", "Error description", highlight="kwargs", tb=traceback.extract_stack())
raise ValueError(error)
```

```
  Some error
  Some error description

  Traceback:
  ├─ <lambda> [61] in .env/lib/python3.6/site-packages/pluggy/manager.py
  ├─── _multicall [187] in .env/lib/python3.6/site-packages/pluggy/callers.py
  └───── pytest_fixture_setup [969] in .env/lib/python3.6/site-packages/_pytest/fixtures.py
         >>> result = call_fixture_func(fixturefunc, request, kwargs)
```

| Argument    | Type     | Description                                                                                | Default |
| ----------- | -------- | ------------------------------------------------------------------------------------------ | ------- |
| `title`     | str      | The message title.                                                                         |         |
| `*texts`    | str      | Optional texts to print (one per line).                                                    |         |
| `highlight` | str      | Optional sequence to highlight in the traceback, e.g. the bad value that caused the error. | `False` |
| `tb`        | iterable | The traceback, e.g. generated by `traceback.extract_stack()`.                              | `None`  |
| **RETURNS** | str      | The formatted traceback. Can be printed or raised by custom exception.                     |         |

### <kbd>class</kbd> `MarkdownRenderer`

Helper to create Markdown-formatted content. Will store the blocks added to the Markdown document in order.

```python
from wasabi import MarkdownRenderer

md = MarkdownRenderer()
md.add(md.title(1, "Hello world"))
md.add("This is a paragraph")
print(md.text)
```

### <kbd>method</kbd> `MarkdownRenderer.__init__`

Initialize a Markdown renderer.

```python
from wasabi import MarkdownRenderer

md = MarkdownRenderer()
```

| Argument    | Type               | Description                    | Default |
| ----------- | ------------------ | ------------------------------ | ------- |
| `no_emoji`  | bool               | Don't include emoji in titles. | `False` |
| **RETURNS** | `MarkdownRenderer` | The renderer.                  |

### <kbd>method</kbd> `MarkdownRenderer.add`

Add a block to the Markdown document.

```python
from wasabi import MarkdownRenderer

md = MarkdownRenderer()
md.add("This is a paragraph")
```

| Argument | Type | Description         | Default |
| -------- | ---- | ------------------- | ------- |
| `text`   | str  | The content to add. |         |

### <kbd>property</kbd> `MarkdownRenderer.text`

The rendered Markdown document.

```python
md = MarkdownRenderer()
md.add("This is a paragraph")
print(md.text)
```

| Argument    | Type | Description                      | Default |
| ----------- | ---- | -------------------------------- | ------- |
| **RETURNS** | str  | The document as a single string. |         |

### <kbd>method</kbd> `MarkdownRenderer.table`

Create a Markdown-formatted table.

```python
md = MarkdownRenderer()
table = md.table([("a", "b"), ("c", "d")], ["Column 1", "Column 2"])
md.add(table)
```

<!-- prettier-ignore -->
```markdown
| Column 1 | Column 2 |
| --- | --- |
| a | b |
| c | d |
```

| Argument    | Type                    | Description                                                                          | Default |
| ----------- | ----------------------- | ------------------------------------------------------------------------------------ | ------- |
| `data`      | Iterable[Iterable[str]] | The body, one iterable per row, containig an interable of column contents.           |         |
| `header`    | Iterable[str]           | The column names.                                                                    |         |
| `aligns`    | Iterable[str]           | Columns alignments in order. `"l"` (left, default), `"r"` (right) or `"c"` (center). | `None`  |
| **RETURNS** | str                     | The table.                                                                           |         |

### <kbd>method</kbd> `MarkdownRenderer.title`

Create a Markdown-formatted heading.

```python
md = MarkdownRenderer()
md.add(md.title(1, "Hello world"))
md.add(md.title(2, "Subheading", "💖"))
```

```markdown
# Hello world

## 💖 Subheading
```

| Argument    | Type | Description                            | Default |
| ----------- | ---- | -------------------------------------- | ------- |
| `level`     | int  | The heading level, e.g. `3` for `###`. |         |
| `text`      | str  | The heading text.                      |         |
| `emoji`     | str  | Optional emoji to show before heading. | `None`  |
| **RETURNS** | str  | The rendered title.                    |         |

### <kbd>method</kbd> `MarkdownRenderer.list`

Create a Markdown-formatted non-nested list.

```python
md = MarkdownRenderer()
md.add(md.list(["item", "other item"]))
md.add(md.list(["first item", "second item"], numbered=True))
```

```markdown
- item
- other item

1. first item
2. second item
```

| Argument    | Type          | Description                     | Default |
| ----------- | ------------- | ------------------------------- | ------- |
| `items`     | Iterable[str] | The list items.                 |         |
| `numbered`  | bool          | Whether to use a numbered list. | `False` |
| **RETURNS** | str           | The rendered list.              |         |

### <kbd>method</kbd> `MarkdownRenderer.link`

Create a Markdown-formatted link.

```python
md = MarkdownRenderer()
md.add(md.link("Google", "https://google.com"))
```

```markdown
[Google](https://google.com)
```

| Argument    | Type | Description        | Default |
| ----------- | ---- | ------------------ | ------- |
| `text`      | str  | The link text.     |         |
| `url`       | str  | The link URL.      |         |
| **RETURNS** | str  | The rendered link. |         |

### <kbd>method</kbd> `MarkdownRenderer.code_block`

Create a Markdown-formatted code block.

```python
md = MarkdownRenderer()
md.add(md.code_block("import spacy", "python"))
```

````markdown
```python
import spacy
```
````

| Argument    | Type | Description              | Default |
| ----------- | ---- | ------------------------ | ------- |
| `text`      | str  | The code text.           |         |
| `lang`      | str  | Optional code language.  | `""`    |
| **RETURNS** | str  | The rendered code block. |         |

### <kbd>method</kbd> `MarkdownRenderer.code`, `MarkdownRenderer.bold`, `MarkdownRenderer.italic`

Create a Markdown-formatted text.

```python
md = MarkdownRenderer()
md.add(md.code("import spacy"))
md.add(md.bold("Hello!"))
md.add(md.italic("Emphasis"))
```

```markdown
`import spacy`

**Hello!**

_Emphasis_
```

### Utilities

#### <kbd>function</kbd> `color`

```python
from wasabi import color

formatted = color("This is a text", fg="white", bg="green", bold=True)
```

| Argument    | Type      | Description                                   | Default |
| ----------- | --------- | --------------------------------------------- | ------- |
| `text`      | str       | The text to be formatted.                     | -       |
| `fg`        | str / int | Foreground color. String name or `0` - `256`. | `None`  |
| `bg`        | str / int | Background color. String name or `0` - `256`. | `None`  |
| `bold`      | bool      | Format the text in bold.                      | `False` |
| `underline` | bool      | Format the text by underlining.               | `False` |
| **RETURNS** | str       | The formatted string.                         |         |

#### <kbd>function</kbd> `wrap`

```python
from wasabi import wrap

wrapped = wrap("Hello world, this is a text.", indent=2)
```

| Argument    | Type | Description                                | Default |
| ----------- | ---- | ------------------------------------------ | ------- |
| `text`      | str  | The text to wrap.                          | -       |
| `wrap_max`  | int  | Maximum line width, including indentation. | `80`    |
| `indent`    | int  | Number of spaces used for indentation.     | `4`     |
| **RETURNS** | str  | The wrapped text with line breaks.         |         |

#### <kbd>function</kbd> `diff_strings`

```python
from wasabi import diff_strings

diff = diff_strings("hello world!", "helloo world")
```

| Argument    | Type      | Description                                                                  | Default            |
| ----------- | --------- | ---------------------------------------------------------------------------- | ------------------ |
| `a`         | str       | The first string to diff.                                                    |
| `b`         | str       | The second string to diff.                                                   |
| `fg`        | str / int | Foreground color. String name or `0` - `256`.                                | `"black"`          |
| `bg`        | tuple     | Background colors as `(insert, delete)` tuple of string name or `0` - `256`. | `("green", "red")` |
| **RETURNS** | str       | The formatted diff.                                                          |                    |

### Environment variables

Wasabi also respects the following environment variables. The prefix can be
customised on the `Printer` via the `env_prefix` argument. For example, setting
`env_prefix="SPACY"` will expect the environment variable `SPACY_LOG_FRIENDLY`.

| Name                   | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| `ANSI_COLORS_DISABLED` | Disable colors.                                        |
| `WASABI_LOG_FRIENDLY`  | Make output nicer for logs (no colors, no animations). |
| `WASABI_NO_PRETTY`     | Disable pretty printing, e.g. colors and icons.        |

## 🔔 Run tests

Fork or clone the repo, make sure you have `pytest` installed and then run it on
the package directory. The tests are located in
[`/wasabi/tests`](/wasabi/tests).

```bash
pip install pytest
cd wasabi
python -m pytest wasabi
```
