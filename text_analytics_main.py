from text_utils import is_palindrome, count_vowels, word_frequency, most_common_word


def main():
    text = input("Enter a paragraph of text:\n")

    print("\n===== TEXT ANALYTICS REPORT =====")
    print(f"Is palindrome: {'yes' if is_palindrome(text) else 'no'}")
    print(f"Vowel count: {count_vowels(text)}")

    # Word frequency table, printed in alphabetical order
    freq = word_frequency(text)
    print("\nWord frequency:")
    for word, count in sorted(freq.items()):
        print(f"  {word}: {count}")

    common = most_common_word(text)
    print(f"\nMost common word: {common if common is not None else 'no words found'}")


if __name__ == "__main__":
    main()