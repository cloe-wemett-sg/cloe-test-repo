def palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def word_wrap(text: str, width: int) -> str:
    words = text.split()
    lines, current = [], []
    length = 0
    for word in words:
        if length + len(word) + (1 if current else 0) > width:
            lines.append(" ".join(current))
            current, length = [word], len(word)
        else:
            length += len(word) + (1 if current else 0)
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines)


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    if len(s) <= max_len:
        return s
    return s[: max_len - len(suffix)] + suffix


def title_case(s: str) -> str:
    minors = {"a", "an", "the", "and", "but", "or", "for", "nor", "on",
              "at", "to", "by", "in", "of", "up"}
    words = s.lower().split()
    result = []
    for i, word in enumerate(words):
        result.append(word if i != 0 and word in minors else word.capitalize())
    return " ".join(result)


def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def snake_to_camel(s: str) -> str:
    parts = s.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def camel_to_snake(s: str) -> str:
    result = []
    for i, ch in enumerate(s):
        if ch.isupper() and i > 0:
            result.append("_")
        result.append(ch.lower())
    return "".join(result)


if __name__ == "__main__":
    print(palindrome("A man a plan a canal Panama"))
    print(caesar_cipher("Hello, World!", 13))
    print(word_wrap("The quick brown fox jumped over the lazy dog", 15))
    print(truncate("This is a very long string", 20))
    print(title_case("the quick brown fox and the lazy dog"))
    print(snake_to_camel("my_variable_name"))
    print(camel_to_snake("myVariableName"))
