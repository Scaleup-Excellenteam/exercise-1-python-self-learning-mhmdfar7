from PIL import Image
import os

def remember_remember(image_path, black_threshold=15, default_char='�'):
    # - Reads hidden message from image pixel data
    # - Looks for near-black pixels (<= threshold)
    # - Uses y-coordinate of black pixels as ASCII codes
    # - Has configurable threshold and default char
    # - Processes image in memory-efficient way

    # Check file exists first
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    try:
        with Image.open(image_path) as img:
            # Convert to RGB for consistent processing
            img = img.convert('RGB')
            pixels = img.load()
            width, height = img.size
            
            # Validate image dimensions
            if width == 0 or height == 0:
                raise ValueError("Invalid image dimensions")
            
            message = []
            
            # Scan image column by column
            for x in range(width):
                # Check pixels bottom-to-top in each column
                for y in reversed(range(height)):
                    r, g, b = pixels[x, y]
                    # Look for near-black pixels
                    if all(c <= black_threshold for c in (r, g, b)):
                        message.append(chr(y))  # Use y-coordinate as char code
                        break
                else:
                    # No black pixel found in this column
                    message.append(default_char)
            
            return ''.join(message)
    
    except (IOError, OSError) as e:
        raise RuntimeError(f"Image processing failed: {str(e)}") from e

if __name__ == '__main__':
    try:
        image_path = os.path.join('resources', 'code.png')
        secret = remember_remember(image_path)
        print("\nDecrypted message:", secret if secret else "DECRYPTION FAILED")
    except Exception as e:
        print(f"Error: {str(e)}")