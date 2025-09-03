# даны строки text и goal
# определить является ли text циклическим сдвигом goal

def rotate_string(text: str, goal: str) -> bool:
    if len(text) != len(goal):
        return False
    return text in goal + goal


if __name__ == "__main__":
    text, goal = 'abcde', 'deabc'
    assert rotate_string(text, goal), f"1. {rotate_string(text, goal)}"
    assert not rotate_string('abcde', 'cdea'), f"2. {rotate_string('abcde', 'cdea')}"
    assert not rotate_string('abcde', 'aaaaa'), f"3. {rotate_string('abcde', 'aaaaa')}"
