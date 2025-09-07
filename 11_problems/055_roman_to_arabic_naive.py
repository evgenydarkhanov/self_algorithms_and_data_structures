r2a = {
   'I': 1,
   'V': 5,
   'X': 10,
   'L': 50,
   'C': 100,
   'D': 500,
   'M': 1000,
}


def roman_to_arabic(roman: str) -> int:
    n = len(roman)
    total = 0

    for i in range(n - 1):
        curr, next_val = r2a[roman[i]], r2a[roman[i + 1]]
        if curr < next_val:
            total -= curr
        else:
            total += curr

    total += r2a[roman[-1]]
    return total


if __name__ == "__main__":
    assert roman_to_arabic('I') == 1, f"{roman_to_arabic('I') = }"
    assert roman_to_arabic('XX') == 20, f"{roman_to_arabic('XX') = }"
    assert roman_to_arabic('XXI') == 21, f"{roman_to_arabic('XXI') = }"
    assert roman_to_arabic('IX') == 9, f"{roman_to_arabic('IX') = }"
    assert roman_to_arabic('XI') == 11, f"{roman_to_arabic('XI') = }"

    assert roman_to_arabic('XVII') == 17, f"{roman_to_arabic('XVII') = }"
    assert roman_to_arabic('XXIX') == 29, f"{roman_to_arabic('XXIX') = }"
    assert roman_to_arabic('XLIX') == 49, f"{roman_to_arabic('XLIX') = }"
    assert roman_to_arabic('IV') == 4, f"{roman_to_arabic('IV') = }"
    assert roman_to_arabic('VI') == 6, f"{roman_to_arabic('VI') = }"

    assert roman_to_arabic('MMDCLXXVI') == 2676, f"{roman_to_arabic('MMDCLXXVI') = }"
    assert roman_to_arabic('MCCCLIX') == 1359, f"{roman_to_arabic('MCCCLIX') = }"
