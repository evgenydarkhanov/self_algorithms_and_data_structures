def fibonacci(n: int, cache=None) -> int:
    if cache is None:
        cache = {}
    if n == 0:
        return 0
    if n < 2:
        return 1

    if (n - 1) in cache:
        n_1 = cache[n - 1]
    else:
        n_1 = fibonacci(n - 1, cache=cache)
        cache[n - 1] = n_1

    if (n - 2) in cache:
        n_2 = cache[n - 2]
    else:
        n_2 = fibonacci(n - 2, cache=cache)
        cache[n - 2] = n_2

    return n_1 + n_2


if __name__ == "__main__":
    assert fibonacci(0) == 0, f"{fibonacci(0) = }"
    assert fibonacci(1) == 1, f"{fibonacci(1) = }"
    assert fibonacci(2) == 1, f"{fibonacci(2) = }"
    assert fibonacci(3) == 2, f"{fibonacci(3) = }"
    assert fibonacci(4) == 3, f"{fibonacci(4) = }"
    assert fibonacci(5) == 5, f"{fibonacci(5) = }"
    assert fibonacci(6) == 8, f"{fibonacci(6) = }"
