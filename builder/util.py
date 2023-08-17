


def set_term_title(title):
    """Sets the title of a POSIX terminal using escape codes.

    Args:
        param1 (str) title: the string to use as the terminal title.

    """
    print("\033]0;{}\a".format(title))


def print_success_message(message):
    print("\x1b[32m{}\x1b[0m".format(message))


def print_fail_message(message):
    print("\x1b[31m{}\x1b[0m".format(message))


def print_checkmark():
    print(u'\x1b[32m\u2713\x1b[0m', end=" ")

def print_crossmark():
    print(u'\x1b[31m\u2717\x1b[0m', end=" ")

if __name__ == "__main__":
    set_term_title("Test1")
    print_success_message("Success")
    print_fail_message("Fail")
    print_checkmark()
    print_crossmark()
