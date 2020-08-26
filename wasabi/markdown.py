# coding: utf8
from __future__ import unicode_literals, print_function


class MarkdownRenderer:
    """Simple helper for generating raw Markdown."""

    def __init__(self, no_emoji=False):
        """Initialize the renderer.

        no_emoji (bool): Don't show emoji in titles etc.
        """
        self.data = []
        self.no_emoji = no_emoji

    @property
    def text(self):
        """RETURNS (str): The Markdown document."""
        return "\n\n".join(self.data)

    def add(self, content):
        """Add a string to the Markdown document.

        content (str): Add content to the document.
        """
        self.data.append(content)

    def table(self, data, header):
        """Create a Markdown table.

        data (Iterable[Iterable[str]]): The body, one iterable per row,
            containig an interable of column contents.
        header (Iterable[str]): The column names.
        RETURNS (str): The rendered table.
        """
        head = "| {} |".format(" | ".join(header))
        divider = "| {} |".format(" | ".join("---" for _ in header))
        body = "\n".join("| {} |".format(" | ".join(row)) for row in data)
        return "{}\n{}\n{}".format(head, divider, body)

    def title(self, level, text, emoji=None):
        """Create a Markdown heading.

        level (int): The heading level, e.g. 3 for ###
        text (str): The heading text.
        emoji (str): Optional emoji to show before heading text, if enabled.
        RETURNS (str): The rendered title.
        """
        prefix = "{} ".format(emoji) if emoji and not self.no_emoji else ""
        return "{} {}{}".format("#" * level, prefix, text)

    def list(self, items, numbered=False):
        """Create a non-nested list.

        items (Iterable[str]): The list items.
        numbered (bool): Whether to use a numbered list.
        RETURNS (str): The rendered list.
        """
        content = []
        for i, item in enumerate(items):
            if numbered:
                content.append("{}. {}".format(i + 1, item))
            else:
                content.append("- {}".format(item))
        return "\n".join(content)

    def link(self, text, url):
        """Create a Markdown link.

        text (str): The link text.
        url (str): The link URL.
        RETURNS (str): The rendered link.
        """
        return "[{}]({})".format(text, url)

    def code_block(self, text, lang=""):
        """Create a Markdown code block.

        text (str): The code text.
        lang (str): Optional code language.
        RETURNS (str): The rendered code block.
        """
        return "```{}\n{}\n```".format(lang, text)

    def code(self, text):
        """Create Markdown inline code."""
        return self._wrap(text, "`")

    def bold(self, text):
        """Create bold text."""
        return self._wrap(text, "**")

    def italic(self, text):
        """Create italic text."""
        return self._wrap(text, "_")

    def _wrap(self, text, marker):
        return "{}{}{}".format(marker, text, marker)
