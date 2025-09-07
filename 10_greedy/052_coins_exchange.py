# Для некоторого набора монет M нужно набрать сумму S минимальным числом монет.
# Набор монет и требуемая сумма будут передаваться аргументами функции.
# Предполагается, что набор монет является каноническим, значит greedy подход допустим.

from typing import List


def exchange(coins: List[int], amount: int) -> List:
    result = []
    idx = len(coins) - 1

    while amount > 0 and idx >= 0:
        if amount >= coins[idx]:
            result.append(coins[idx])
            amount -= coins[idx]
        else:
            idx -= 1

    if amount < 0:
        return []

    return result


if __name__ == "__main__":
    assert exchange([1, 2, 5, 10], 11) == [10, 1]
    assert exchange([1, 2, 5], 11) == [5, 5, 1]
    assert exchange([1, 2, 5, 10], 9) == [5, 2, 2]
    assert exchange([2, 5, 10], 1) == []
