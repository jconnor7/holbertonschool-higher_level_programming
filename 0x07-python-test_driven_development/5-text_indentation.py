#!/usr/bin/python3
"""Text indentation
"""


def text_indentation(text):
    """Prints text with 2 new lines after the characters: .?:
    Args:
        Text: text that will be printed.
    Raises:
        TypeError: raises error if text is not a string.
    Note:
        There should be no space at the beginning or
        at the end of each printed line.
        Searches text for special characters and appends new lines,
        converts text to a list and strips the elements of the list
        prints out the text after joining everything together again
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in [".", "?", ":"]:
        if char in text:
            text = text.replace(char, char + "\n\n\a")
    print("\n\n".join([i.strip() for i in text.split("\a")]), end="")
