def group_by(func, iterable):
    # - Groups items from iterable based on function output
    # - Creates dictionary with function results as keys
    # - Values are lists of items that produced each key
    
    result = {}
    for item in iterable:
        key = func(item)  # Get grouping key
        
        # Initialize list if key doesn't exist
        if key not in result:
            result[key] = []
        
        # Add item to its group
        result[key].append(item)
    
    return result

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))