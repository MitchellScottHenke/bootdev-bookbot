import sys
from stats import sorted_character_counts, word_count, character_count

def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
        return book_text
    
def main():
    # if sys.argv doesn't have two entries, return an explanation that there needs to be a filepath
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    else:
        filepath = sys.argv[1]
    frankenstein = get_book_text(filepath)
    counted_words = word_count(frankenstein)
    character_counts = character_count(frankenstein)
    sorted_counts = sorted_character_counts(character_counts)
    print("="*15 + "BOOKBOT" + "="*15)
    print(f"Analyzing book found at {filepath}")
    print("-"*15 + "WORD COUNT" + "-"*15)
    print(f"Found {counted_words} total words")
    print("-"*15 + "CHARACTER COUNT" + "-"*15)
    for char, count in sorted_counts:
        print(f"{char}: {count}")
    
if __name__ == "__main__":
    main()
    
