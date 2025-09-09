# используя хеш-таблицу, определить, является ли строка b анаграммой к строке a
# можно посортировать, но будет O(nlogn)

"""
можно совсем просто
from collections import Counter


def is_anagram(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)
"""


from collections import defaultdict


def is_anagram(a: str, b: str) -> bool:
    """O(n)"""
    if len(a) != len(b):
        return False

    table = defaultdict(int)
    for c in a:
        table[c] += 1

    for c in b:
        if c not in table:
            return False

        table[c] -= 1

        if table[c] == 0:
            del table[c]

    return len(table) == 0


if __name__ == "__main__":
    assert is_anagram('abba', 'abab'), is_anagram('abba', 'abab')
    assert is_anagram('a', 'a'), is_anagram('a', 'a')
    assert is_anagram('abcd', 'dcba'), is_anagram('abcd', 'dcba')
    assert not is_anagram('abb', 'aab'), is_anagram('abb', 'aab')
    assert not is_anagram('abbaa', 'abab'), is_anagram('abbaa', 'abab')
