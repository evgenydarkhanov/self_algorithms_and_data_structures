def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    assert fibonacci(0) == 0, f"{fibonacci(0) = }"
    assert fibonacci(1) == 1, f"{fibonacci(1) = }"
    assert fibonacci(2) == 1, f"{fibonacci(2) = }"
    assert fibonacci(3) == 2, f"{fibonacci(3) = }"
    assert fibonacci(4) == 3, f"{fibonacci(4) = }"
    assert fibonacci(5) == 5, f"{fibonacci(5) = }"
    assert fibonacci(6) == 8, f"{fibonacci(6) = }"
