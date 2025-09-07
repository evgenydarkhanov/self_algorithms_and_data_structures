def d(s1: str, s2: str, i: int, j: int) -> int:
    if i > 0 and j > 0:
        m = 1
        if s1[i] == s2[j]:
            m = 0
        return min(
            d(s1, s2, i, j-1) + 1,
            d(s1, s2, i-1, j) + 1,
            d(s1, s2, i-1, j-1) + m,
        )
    elif i == 0 and j == 0:
        return 0
    elif i == 0 and j != 0:
        return j
    else:
        return i


def levenshtein(s1: str, s2: str) -> int:
    s1 = ' ' + s1
    s2 = ' ' + s2
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            dp[i][j] = d(s1, s2, i, j)

    return dp[-1][-1]


if __name__ == "__main__":
    assert levenshtein('гибралтар', 'лабрадор') == 5
    assert levenshtein('строка', 'собака') == 3
    assert levenshtein('мама', 'мыла') == 2
    assert levenshtein('мама', 'раму') == 2
    assert levenshtein('мама', 'папа') == 2
