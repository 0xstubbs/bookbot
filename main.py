from stats import get_wordcount, get_symbol_count, get_sorted
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        filepath = sys.argv[1]
        word_count = get_wordcount(filepath)
        print(f"{word_count} words found in the document")

        symbol_count = get_symbol_count(filepath)
        # print(symbol_count)
        sorted_char_count = get_sorted(filepath)

        bookbot_header = "============ BOOKBOT ============"
        wordcount_header = "----------- Word Count ----------\n"
        wordcount_text = f"Found {word_count} total words\n"
        charcount_header = "--------- Character Count -------"
        print(
            f"{bookbot_header}\nAnalyzing book found at {filepath}...\n{wordcount_header}{wordcount_text}{charcount_header}"
        )
        for item in sorted_char_count:
            print(f"{item['char']}: {item['count']}")
        print("============= END ===============")


main()
