


def set_term_title(title):
    """Sets the title of a POSIX terminal using escape codes.

    Args:
        param1 (str) title: the string to use as the terminal title.

    """
    print("\033]0;{}\a".format(title))

    