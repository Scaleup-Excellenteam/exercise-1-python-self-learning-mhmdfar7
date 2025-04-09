def long_cat_is_long(text):
    # - Cleans text and creates word-length dictionary
    # - First checks if input is actually a string
    # - Handles empty/whitespace strings
    # - Uses list comprehension for cleaning words
    # - Dict comprehension for final output
    # - Filters out empty strings at the end

    # Input validation
    if not isinstance(text, str):  # Reject non-string inputs
        return {}
    if not text.strip():  # Handle empty/whitespace strings
        return {}
    
    # Clean each word - keep only alphabetic chars
    cleaned_words = [
        ''.join(c for c in word if c.isalpha())  # Filter non-letters
        for word in text.split()  # Split into words
    ]
    
    # Create {word:length} dictionary
    return {word: len(word) for word in cleaned_words if word}  # Skip empty words

if __name__ == '__main__':
    print(long_cat_is_long("Hello, world! Test123."))  
    print(long_cat_is_long(""))  
    print(long_cat_is_long(123)) 