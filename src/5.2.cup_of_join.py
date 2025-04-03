def cup_of_join(*args, sep=None):
    # - Joins multiple lists together with optional separator
    # - First checks if we got any arguments at all
    # - Verifies all args are lists (strict typing)
    # - Uses extend() to merge lists efficiently
    # - Adds separator between lists if provided
    # - Returns None for invalid inputs
    
    # Handle empty input case
    if not args:
        return None
    
    # Type checking - all must be lists
    if not all(isinstance(lst, list) for lst in args):
        return None

    result = []
    for lst in args:
        # Merge current list into result
        result.extend(lst)
        
        # Add separator if provided
        if sep is not None:
            result.append(sep) 
    
    # Final result contains all elements with separators
    return result

if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))  
    print(cup_of_join([1, 2], [8], [9, 5, 6]))           
    print(cup_of_join([1]))                              
    print(cup_of_join())                                  