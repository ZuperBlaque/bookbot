# Get the number of words in a book 
def get_number_of_words(book_text):
    words = book_text.split()
    return len(words)

#Building a character count function
def character_count(book_text):
    #first we will create a dictionary to hold the character counts
    list_of_characters = {}
    #then we will loop through each character in the book text and count how many times each character appears
    #automatically will also ignore spaces and punctuation
    for character in book_text:
        #we will convert each character to lowercase to ensure that 'A' and 'a' are counted as the same character
        character = character.lower()
        if character in list_of_characters:
            list_of_characters[character] += 1
        else:
            list_of_characters[character] = 1
    return list_of_characters

def sort_character_counts(character_counts):
    #first we will convert the dictionary to a list of tuples
    sorted_counts = [
        {"char": char, "num": count}
        for char, count in character_counts.items()
        if char.isalpha()
    ]
    sorted_counts.sort(key=lambda x: x["num"], reverse=True)
    return sorted_counts
  