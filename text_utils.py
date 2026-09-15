import re

def is_palindrome(s):
    cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]

def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def word_frequency(s):
    freq = {}
    for word in re.findall(r"[a-z0-9]+", s.lower()):
        freq[word] = freq.get(word, 0) + 1
    return freq

def most_common_word(s):
    freq = word_frequency(s)
    if not freq:
        return None
    return max(freq.items(), key=lambda item: item[1])[0]

if __name__ == "__main__":

    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("hello") is False
    assert count_vowels("Hello World") == 3
    assert word_frequency("The cat and the dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1}
    assert most_common_word("apple banana apple cherry apple") == "apple"
    print("text_utils self-tests passed")