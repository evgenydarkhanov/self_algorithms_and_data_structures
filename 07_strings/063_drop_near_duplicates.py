"""
Дана строка s. Строка состоит из английских букв в нижнем регистре. Необходимо из строки удалить все рядом стоящие повторяющиеся буквы.
Например, в строке xyyx мы должны удалить yy, а после и оставшиеся xx итого после должна получиться пустая строка.
Или же в строке fqffqzzsd после удаления остануться только fsd. Первыми удалятся ff, являющиеся третьим и четвертым символами, затем qq и после уже zz.
"""

def drop_near_duplicates(string: str) -> str:
    stack = []
    for c in string:
        if not stack:
            stack.append(c)
        else:
            c_ = stack.pop()
            if c == c_:
                continue
            else:
                stack.append(c_)
                stack.append(c)

    return ''.join(stack)


if __name__ == "__main__":
    assert drop_near_duplicates('xyyx') == ''
    assert drop_near_duplicates('fqffqzzsd') == 'fsd'
    assert drop_near_duplicates('aa') == ''
    assert drop_near_duplicates('aaa') == 'a'
    assert drop_near_duplicates('aza') == 'aza'
    assert drop_near_duplicates('') == ''
    assert drop_near_duplicates('abcd') == 'abcd'
    assert drop_near_duplicates('aaaa') == ''
    assert drop_near_duplicates('a') == 'a'
