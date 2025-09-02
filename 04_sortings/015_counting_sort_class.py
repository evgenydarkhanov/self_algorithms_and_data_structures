import random
from dataclasses import dataclass
from typing import List


@dataclass(order=True)
class Person:
    name: str = ''
    surname: str = ''
    age: int = 0
    address: str = ''


def counting_sort(arr: List[Person], key) -> List[Person]:
    n = len(arr)
    m = max(key(p) for p in arr)

    out = [None for _ in range(n)]
    tmp = [0 for _ in range(m + 1)]

    for elem in arr:
        tmp[key(elem)] += 1

    for i in range(1, m + 1):
        tmp[i] += tmp[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        elem = key(arr[i])
        index = tmp[elem] - 1
        out[index] = arr[i]
        tmp[elem] -= 1

    return out
 

if __name__ == "__main__":
    persons = [
        Person(age=random.randint(10, 50))
        for _ in range(10)
    ]

    arr_reference = sorted(persons, key=lambda x: x.age)
    arr_custom = counting_sort(persons, key=lambda x: x.age)

    assert arr_custom == arr_reference, f'{arr_custom}'
