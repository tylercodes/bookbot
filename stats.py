def number_of_words(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in.
    :return: The number of words in the text.
    """
    words = text.split()
    return len(words)

def number_of_each_character(text):
    """
    Counts the number of occurrences of each character in a given text, treating all characters as lowercase.
    
    :param text: The text to count characters in.
    :return: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}
    for char in text.lower():  # Convert each character to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    """
    Sorts the character count dictionary by count in descending order, including all characters.
    
    :param char_count: The dictionary with characters as keys and their counts as values.
    :return: A sorted list of tuples (character, count).
    """
    return sorted(
        char_count.items(),  # Use all items from the dictionary
        key=lambda item: item[1],  # Sort by count (second element of the tuple)
        reverse=True  # Sort in descending order
    )