import re

# Text-analysis helpers used by text_analytics_main.py


def is_palindrome(s):
    """Return True if s reads the same forwards and backwards
    (ignoring case and non-alphanumeric characters)."""
    cleaned = re.sub(r"[^a-z0-9]", "", s.lower())  # keep only letters/digits
    return cleaned == cleaned[::-1]


def count_vowels(s):
    """Count the vowel characters in s."""
    return sum(1 for ch in s.lower() if ch in "aeiou")


def word_frequency(s):
    """Return a dict mapping each word in s to its number of occurrences."""
    freq = {}
    for word in re.findall(r"[a-z0-9]+", s.lower()):
        freq[word] = freq.get(word, 0) + 1
    return freq


def most_common_word(s):
    """Return the most frequent word in s, or None if there are no words."""
    freq = word_frequency(s)
    if not freq:
        return None
    return max(freq.items(), key=lambda item: item[1])[0]


if __name__ == "__main__":
    # Simple self-tests for the helpers above
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("hello") is False
    assert count_vowels("Hello World") == 3
    assert word_frequency("The cat and the dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1}
    assert most_common_word("apple banana apple cherry apple") == "apple"
    print("text_utils self-tests passed")