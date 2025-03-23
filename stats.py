def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_wordcount(filepath):
    book_contents = get_book_text(filepath).split()
    word_count = len(book_contents)
    return word_count


def get_symbol_count(filepath):
    book_contents = get_book_text(filepath).lower().strip()
    unique_symbols = set(book_contents)
    symbol_dict = dict.fromkeys(unique_symbols, 0)

    for character in book_contents:
        count = symbol_dict[character]
        new_count = count + 1
        symbol_dict[character] = new_count

    return symbol_dict


def get_sorted(filepath):
    symbol_count = get_symbol_count(filepath)
    character_list = []
    for char in symbol_count:
        # print(f"{item}: {symbol_count[item]}")
        if char.isalpha():
            character_list.append({"char": char, "count": symbol_count[char]})

    def sort_on(dict):
        return dict["count"]

    character_list.sort(
        reverse=True, key=sort_on
    )  # print(sorted(symbol_count, reverse=True))
    # print(character_list)
    return character_list
