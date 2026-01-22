def factorial_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError()

    if n < 0:
        raise ValueError()

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)



