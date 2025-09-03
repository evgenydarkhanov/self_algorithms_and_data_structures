def naive_search(text: str, pattern: str) -> int:
    """O(n * m)"""
    n = len(text)
    m = len(pattern)
    if m > n:
        return -1

    for i in range(n - m + 1):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
            if j == m - 1:
                return i
    return -1


if __name__ == "__main__":
    assert naive_search('aaabbbaaa', 'abb') == 2, f"{naive_search('aaabbbaaa', 'abb') = }"
    assert naive_search('aaabbbaaa', 'cc') == -1, f"{naive_search('aaabbbaaa', 'cc') = }"
    assert naive_search('aaabba', 'abbaaaaaa') == -1, f"{naive_search('aaabba', 'abbaaaaaa') = }"
    assert naive_search('aabbbaaa', 'aaa') == 5, f"{naive_search('aabbbaaa', 'aaa') = }"
