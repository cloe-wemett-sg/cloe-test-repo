from typing import Any


def flatten(nested: list, depth: int = -1) -> list:
    result = []
    for item in nested:
        if isinstance(item, list) and depth != 0:
            result.extend(flatten(item, depth - 1))
        else:
            result.append(item)
    return result


def chunk(lst: list, size: int) -> list[list]:
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def group_by(lst: list[dict], key: str) -> dict[Any, list]:
    groups: dict = {}
    for item in lst:
        k = item.get(key)
        groups.setdefault(k, []).append(item)
    return groups


def unique(lst: list) -> list:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def frequency_map(lst: list) -> dict:
    counts: dict = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts


def zip_to_dict(keys: list, values: list) -> dict:
    if len(keys) != len(values):
        raise ValueError("Keys and values must have the same length")
    return dict(zip(keys, values))


def deep_merge(base: dict, override: dict) -> dict:
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


if __name__ == "__main__":
    print(flatten([1, [2, [3, [4]]], 5]))
    print(chunk(list(range(10)), 3))

    people = [
        {"name": "Alice", "dept": "eng"},
        {"name": "Bob", "dept": "eng"},
        {"name": "Carol", "dept": "design"},
    ]
    print(group_by(people, "dept"))

    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    print(frequency_map(words))

    base = {"a": 1, "b": {"x": 10, "y": 20}}
    override = {"b": {"y": 99, "z": 30}, "c": 3}
    print(deep_merge(base, override))
