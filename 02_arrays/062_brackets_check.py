# проверка валидности скобок
# '({[]})' - True
# '{[}' - False

mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def brackets_check(brackets: str) -> bool:
    stack = []
    for b in brackets:
        if b in mapping:
            stack.append(b)

        elif len(stack) == 0 or b != mapping[stack.pop()]:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    assert brackets_check('()'), brackets_check('()')
    assert not brackets_check('(]'), brackets_check('(]')
    assert brackets_check('{{{[()]}}}'), brackets_check('{{{[()]}}}')
    assert not brackets_check('([{{{)'), brackets_check('([{{{)')
