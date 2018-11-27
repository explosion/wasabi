# wasabi: A lightweight console printing and formatting toolkit

Over the years, I've written countless implementations of coloring and
formatting utilities to output messages in our libraries like
[spaCy](https://spacy.io), [Thinc](https://github.com/explosion/thinc) and
[Prodigy](https://prodi.gy). While there are many other great open-source
options, I've always ended up wanting something slightly different or slightly
custom.

This package is still a work in progress and aims to bundle those utilities in
a standardised way so they can be shared across our other projects. It's super
lightweight, has zero dependencies and works across Python 2 and 3.

[![Travis](https://img.shields.io/travis/ines/wasabi/master.svg?style=flat-square&logo=travis)](https://travis-ci.org/ines/wasabi)
[![Appveyor](https://img.shields.io/appveyor/ci/inesmontani/wasabi/master.svg?style=flat-square&logo=appveyor)](https://ci.appveyor.com/project/inesmontani/wasabi)
[![PyPi](https://img.shields.io/pypi/v/wasabi.svg?style=flat-square)](https://pypi.python.org/pypi/wasabi)
[![GitHub](https://img.shields.io/github/release/ines/wasabi/all.svg?style=flat-square)](https://github.com/ines/wasabi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

<img width="609" src="https://user-images.githubusercontent.com/13643239/48663861-8c9ea000-ea96-11e8-8b04-d120c52276a8.png">

## 💬 FAQ

### Are you going to add more features?

Yes, there's still a bunch of helpers and features to port over – for example,
[Thinc](https://github.com/explosion/thinc)'s custom traceback printer. I'd also
love to add a nice training results table utility, since this is something that
we use a lot.

However, the new features will be heavily biased by what we (think we) need. I
always appreciate pull requests to improve the existing functionality – but I
want to keep this library as simple, lightweight and specific as possible.

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

I was looking for a short and descriptive name, but everything was already taken.
So I ended up naming this package after one of my rats, Wasabi. 🐀

## ⌛️ Installation

```bash
pip install wasabi
```

## 🎛 API

### <kbd>class</kbd> `Printer`

#### <kbd>method</kbd> `Printer.__init__`

```python
from wasabi import Printer

msg = Printer()
```

| Argument | Type | Description | Default |
| --- | --- | --- | -- |
| `pretty` | bool | Pretty-print output with colors and icons. | `True` |
| `no_print` | bool | Don't actually print, just return. | `False` |
| `colors` | dict | Add or overwrite color values, names mapped to `0`-`256`. | `None` |
| `icons` | dict | Add or overwrite icon. Name mapped to unicode. | `None` |
| `line_max` | int | Maximum line length (for divider). | `80` |
| `animation` | unicode | Steps of loading animation for `Printer.loading`. | `"⠙⠹⠸⠼⠴⠦⠧⠇⠏"` |
| `animation_ascii` | unicode | Alternative animation for ASCII terminals. | `"\|/-\\"` |
| `ignore_warnings` | bool | Don't output messages of type `MESSAGE.WARN`. | `False` |
| **RETURNS** | `Printer` | The initialized printer. | - |

#### <kbd>method</kbd> `Printer.text`

```python
msg = Printer()
msg.text("Hello world!")
```

| Argument | Type | Description | Default |
| --- | --- | --- | -- |
| `title` | unicode | The main text to print. | `""` |
| `text` | unicode | Optional additional text to print. | `""` |
| `color` | unicode / int | Color name or value. | `None` |
| `icon` | unicode | Name of icon to add. | `None` |
| `show` | bool | Whether to print or not. Can be used to only output messages under certain condition, e.g. if `--verbose` flag is set. | `True` |
| `no_print` | bool | Don't actually print, just return. Overwrites global setting. | `False` |
| `exits` | int | If set, perform a system exit with the given code after printing. | `None` |

#### <kbd>method</kbd> `Printer.good`, `Printer.fail`, `Printer.warn`, `Printer.info`

Print special formatted messages.

```python
msg = Printer()
msg.good("Success")
msg.fail("Error")
msg.warn("Warning")
msg.info("Info")
```

| Argument | Type | Description | Default |
| --- | --- | --- | -- |
| `title` | unicode | The main text to print. | `""` |
| `text` | unicode | Optional additional text to print. | `""` |
| `show` | bool | Whether to print or not. Can be used to only output messages under certain condition, e.g. if `--verbose` flag is set. | `True` |
| `exits` | int | If set, perform a system exit with the given code after printing. | `None` |

#### <kbd>method</kbd> `Printer.divider`

Print a formatted divider.

```python
msg = Printer()
msg.divider("Heading")
```
| Argument | Type | Description | Default |
| --- | --- | --- | -- |
| `text` | unicode | Headline text. If empty, only the line is printed. | `""` |
| `char` | unicode | Single line character to repeat. | `"="` |
| `show` | bool | Whether to print or not. Can be used to only output messages under certain condition, e.g. if `--verbose` flag is set. | `True` |

#### <kbd>contextmanager</kbd> `Printer.loading`

```python
msg = Printer()
with msg.loading("Loading..."):
    # Do something here that takes longer
    time.sleep(10)
msg.good("Successfully loaded something!")
```

| Argument | Type | Description | Default |
| --- | --- | --- | -- |
| `text` | unicode | The text to display while loading. | `""` |

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

| Argument | Type | Description |
| --- | --- | --- |
| **RETURNS** | `Counter` | The counts for the individual special message types. |

### Utilities

#### <kbd>function</kbd> `color`

```python
from wasabi import color

formatted = color("This is a text", fg="white", bg="green", bold=True)
```

| Argument | Type | Description | Default |
| --- | --- | --- | -- |
| `text` | unicode | The text to be formatted. | - |
| `fg` | unicode / int | Foreground color. String name or `0` - `256`. | `None` |
| `bg` | unicode / int | Background color. String name or `0` - `256`. | `None` |
| `bold` | bool | Format the text in bold. | `False` |
| **RETURNS** | unicode | The formatted string. | |

#### <kbd>function</kbd> `wrap`

```python
from wasabi import wrap

wrapped = wrap("Hello world, this is a text.", indent=2)
```

| Argument | Type | Description | Default |
| --- | --- | --- | -- |
| `text` | unicode | The text to wrap. | - |
| `wrap_max` | int | Maximum line width, including indentation. | `80` |
| `indent` | int | Number of spaces used for indentation. | `4` |
| **RETURNS** | unicode | The wrapped text with line breaks.

## 🔔 Run tests

Fork or clone the repo, make sure you have `pytest` installed and then run it
on the directory [`/tests`](/tests):

```bash
pip install pytest
cd wasabi
python -m pytest tests
```
