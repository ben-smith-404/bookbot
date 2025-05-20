import sys
from stats import get_num_words,count_character_occurance,sort_character_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    content = get_book_text(path_to_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(content)} total words")
    print("----------- Character Count ----------")
    for dict in sort_character_dictionary(count_character_occurance(content)):
        if str.isalpha(dict["char"]):
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()