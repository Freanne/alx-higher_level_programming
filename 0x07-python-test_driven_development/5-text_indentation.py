#!/usr/bin/python3
"""Define text_indentation function """


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If `text` is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = text.split('.')
    sentences = [sentence.strip() for sentence in sentences if sentence.strip() != '']
    sentences = '.'.join(sentences).split('?')
    sentences = [sentence.strip() for sentence in sentences if sentence.strip() != '']
    sentences = '?'.join(sentences).split(':')
    sentences = [sentence.strip() for sentence in sentences if sentence.strip() != '']

    for sentence in sentences:
        print(sentence)
        print()
