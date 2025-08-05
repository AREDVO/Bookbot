import sys

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
from stats import get_num_words   
from stats import get_num_characters 
from stats import sorted_list
from stats import sort_on

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]

    book_content = get_book_text(path_to_file)

    words = get_num_words(book_content)

    cleaned_text = book_content.replace('\n', ' ').replace('\r', ' ')
    letters = get_num_characters(cleaned_text)

    #print(letters)

    sorted_letters = sorted_list(letters)
    sorted_letters.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")

    print("============= END ===============")

main()
