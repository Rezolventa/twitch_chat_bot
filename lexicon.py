
def decline_count(count):
    """Склоняет слово раз."""
    if (
        2 <= count % 10 <= 4
        and count % 100 != 12
        and count % 100 != 13
        and count % 100 != 14
    ):
        return "раза"
    return "раз"
