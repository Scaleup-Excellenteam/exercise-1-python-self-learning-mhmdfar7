import re
import os

def parsle_tongue(file_path=None, chunk_size=4096, default_file='../resources/logo.jpg', encoding='latin-1'):
    # - Finds all 5+ letter lowercase words in a binary file
    # - Reads file in chunks for memory efficiency
    # - Has sensible defaults but allows customization
    # - Uses regex to find valid words
    # - Handles encoding issues gracefully

    # Validate chunk size
    if not isinstance(chunk_size, int) or chunk_size <= 0:
        chunk_size = 4096  # Default to 4KB chunks
    
    # Set default file path if none provided
    if file_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, default_file)
    
    # Skip if path is directory
    if os.path.isdir(file_path):
        return []

    # Compile regex once for efficiency
    pattern = re.compile(r'([a-z]{5,})')  # Finds 5+ letter words
    buffer = ''  # Stores incomplete chunks
    messages = set()  # Using set to avoid duplicates

    try:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:  # End of file
                    break
                
                # Try decoding chunk
                try:
                    decoded_chunk = chunk.decode(encoding, errors='ignore')
                except UnicodeDecodeError:
                    continue  # Skip bad chunks
                
                # Combine with previous buffer
                combined = buffer + decoded_chunk
                
                # Find all matches in combined text
                for match in pattern.finditer(combined):
                    messages.add(match.group(1))
                
                # Store remaining text for next chunk
                buffer = combined[match.end()] if match else combined

        return sorted(messages)  # Return sorted list
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

if __name__ == '__main__':
    secret_messages = parsle_tongue()
    print("Found messages:", secret_messages)