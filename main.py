from stats import number_of_words
from stats import number_of_each_character
from stats import sort_char_count
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = number_of_words(book_text)
    char_count = number_of_each_character(book_text)
    sorted_list = sort_char_count(char_count)
    print_report(book_path, num_words, sorted_list)

# This script reads a text file containing the book "Frankenstein" and prints its contents to the console.
def get_book_text(file):
    """
    Reads the contents of a text file and returns it as a string.
    
    :param file: The path to the text file.
    :return: The contents of the file as a string.
    """
    with open(file) as f:
        contents = f.read()
        return contents 

def print_report(book_path, num_words, sorted_list):
    """
    Prints a report of the book's statistics.
    
    :param book_path: The path to the book file.
    :param num_words: The number of words in the book.
    :param sorted_list: A sorted list of character counts.
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----")
    for item in sorted_list:
        if not item[0].isalpha():
            continue
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

main()