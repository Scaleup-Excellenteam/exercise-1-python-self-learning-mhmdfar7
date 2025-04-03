import os

def thats_the_way(directory, prefix="deep"):
    # - Finds files starting with given prefix in a directory
    # - First checks if directory is valid string and exists
    # - Uses list comprehension for clean filtering
    # - Handles permission errors gracefully
    # - Default prefix is "deep" (configurable)
    # - Returns empty list if any problems occur (safe default)
    if not directory or not isinstance(directory, str):
        return []
    
    try:
        if not os.path.isdir(directory):
            return []
        
        # 1. Lists all files in directory
        # 2. Checks prefix match
        # 3. Verifies it's a file (not subdirectory)
        return [
            f
            for f in os.listdir(directory) 
            if f.startswith(prefix) and os.path.isfile(os.path.join(directory, f))
        ]
    except (PermissionError, FileNotFoundError):
        return [] 

if __name__ == '__main__':
    directory_path = input("Enter directory path: ")
    print(thats_the_way(directory_path))