# можно не делать отдельную функцию для подсчёта элемента матрицы
# можно не хранить всю матрицу

def levenshtein(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    curr_row = range(m + 1)
    for i in range(n + 1):
        prev_row, curr_row = curr_row, [i] + [0] * m
        for j in range(1, m + 1):
            add, delete, change = prev_row[j] + 1, curr_row[j - 1] + 1, prev_row[j - 1]

            if s1[j - 1] != s2[i - 1]:
                change += 1

            curr_row[j] = min(add, delete, change)

    return curr_row[-1]


if __name__ == "__main__":
    assert levenshtein('гибралтар', 'лабрадор') == 5
    assert levenshtein('строка', 'собака') == 3
    assert levenshtein('мама', 'мыла') == 2
    assert levenshtein('мама', 'раму') == 2
    assert levenshtein('мама', 'папа') == 2
