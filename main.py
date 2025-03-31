from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        novel = f.read()

    return novel

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    novel = get_book_text(filepath)
    num_words = count_words(novel)
    num_chars = count_chars(novel)
    sorted_chars = sort_chars(num_chars)

    # Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")

main()
