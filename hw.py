from typing import Union

# 1 задание


def is_palindrome(origin: Union[str, int], /) -> bool:
    """
    Usage:
    >>> assert is_palindrome("aba") is True
    >>> assert is_palindrome("abc") is False
    >>> assert is_palindrome(12345) is False
    >>> assert is_palindrome(12321) is True
    >>> assert is_palindrome("Hannah") is True
    >>> assert is_palindrome("Do geese see God?") is True
    """
    origin = str(origin)
    origin = origin.lower()
    origin = "".join(c for c in origin if c.isalnum())  # Убрать из строки все спец символы
    return origin == origin[::-1]

# 3 задание


def are_parentheses_balanced(origin: str, /) -> bool:
    """
    Usage:
    >>> assert are_parentheses_balanced("({[]})") is True
    >>> assert are_parentheses_balanced(")]}{[(") is False
    """
    div = []
    open = ['(', '[', '{', '<']
    close = [')', ']', '}', '>']

    for char in origin:
        if char in open:
            div.append(char)
        elif char in close:
            if not div:
                return False
            open_bracket = div.pop()
            if open.index(open_bracket) != close.index(char):
                return False

    return len(div) == 0

# 4 задание


def get_longest_uniq_length(origin: str, /) -> int:
    """
    Usage:
    >>> assert get_longest_uniq_length("abcdefg") == 7
    >>> assert get_longest_uniq_length("racecar") == 4
    """
    max_length = 0
    current_length = 0
    symbols = set()

    for i in origin:
        if i not in symbols:
            current_length += 1
            symbols.add(i)
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
            symbols = {i}

    if current_length > max_length:
        max_length = current_length

    return max_length
