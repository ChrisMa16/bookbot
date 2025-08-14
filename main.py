from stats import count_words
from stats import char_count
from stats import list_dict
import sys


def get_book_text(filepath):
    with open(filepath,"r") as f:
        file_contents = f.read()
        return file_contents

    

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        opened_book = get_book_text(sys.argv[1])
    print(f"Total characters: {len(opened_book)}")
    counted_words = count_words(opened_book)
    print(f"{counted_words} words found in the document")
    counted_characters = char_count(opened_book)
    print(f"{counted_characters}")
    new_report = list_dict(counted_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {counted_words} total words")
    print("--------- Character Count -------")
    for dictionary in new_report:
        if dictionary["char"].isalpha():
            print(f'{dictionary["char"]}: {dictionary["num"]}')
    print("============= END ===============")



main()

