# Given an integer x, return true if x is a palindrome, and false otherwise.

def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    original = x
    reversed_x = 0
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10

    return original == reversed_x


if __name__ == "__main__":
    assert is_palindrome(121), f"{is_palindrome(121) = }"
    assert is_palindrome(12121), f"{is_palindrome(12121) = }"
    assert not is_palindrome(12121407), f"{is_palindrome(12121407) = }"
    assert not is_palindrome(121214070), f"{is_palindrome(121214070) = }"
    assert is_palindrome(11111111), f"{is_palindrome(11111111) = }"
    assert is_palindrome(5555), f"{is_palindrome(5555) = }"
    assert not is_palindrome(1234), f"{is_palindrome(1234) = }"
    assert is_palindrome(987656789), f"{is_palindrome(987656789) = }"
    assert not is_palindrome(-121), f"{is_palindrome(-121) = }"
    assert not is_palindrome(10), f"{is_palindrome(10) = }"
