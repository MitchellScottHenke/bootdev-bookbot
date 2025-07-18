# Takes a string and returns the number of words in it    
def word_count(text):
    words = text.split()
    return len(words)

# Counts the number of usages of each character in the text
def character_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

# Sorts the character counts by frequency
def sorted_character_counts(character_counts):
    return sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
