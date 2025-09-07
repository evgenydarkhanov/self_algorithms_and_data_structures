"""
Дана строка s, найти длину наибольшей подстроки, содержащую уникальные символы (без повторений).

Пример 1
Ввод: "abcabcbb"
Вывод: 3

Пример 2
Ввод: "pwwhkew"
Вывод: 4

Пример 3
Ввод: "abcdef"
Вывод: 6

sliding window
"""

def longest_unique_substring(string: str) -> int:
    n = len(string)
    seen = set()
    l = r = max_length = 0
    while l < n and r < n:
        if string[r] not in seen:
            seen.add(string[r])
            r += 1
            max_length = max(max_length, r - l)
        else:
            seen.remove(string[l])
            l += 1

    return max_length


if __name__ == "__main__":
    assert longest_unique_substring("abcabcbb") == 3, f"{longest_unique_substring('abcabcbb') = }"
    assert longest_unique_substring("pwwhkew") == 4, f"{longest_unique_substring('pwwhkew') = }"
    assert longest_unique_substring("abcdef") == 6, f"{longest_unique_substring('abcdef') = }"
