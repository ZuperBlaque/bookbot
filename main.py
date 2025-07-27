from stats import get_number_of_words

from stats import character_count

from stats import sort_character_counts

# Built in sys module provides access to command line arguments
# list of strings representing the arguments passed to the script. 
# The first argument is the script name, the rest are the arguments.
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:  
        book_text = get_book_text(sys.argv[1])
    word_count = get_number_of_words(book_text)
    character_counts = character_count(book_text)
    
    # call the sort_character_counts function to sort the character counts
    sorted_char_counts = sort_character_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("---------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count --------")
    # Print the sorted character counts
    # iterate through the sorted character counts and print each character with its count
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()