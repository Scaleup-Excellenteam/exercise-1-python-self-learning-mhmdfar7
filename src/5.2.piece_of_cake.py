def piece_of_cake(prices, optionals=None, **kwargs):
    # - Calculates total price based on ingredient prices and quantities
    # - First validates prices is a dict with numeric values
    # - Handles optional ingredients that shouldn't be charged
    # - Validates all amounts are positive numbers
    # - Returns 0.0 for any invalid inputs (safe default)
    # - Uses kwargs for flexible ingredient inputs

    # Validate prices dictionary
    if not isinstance(prices, dict) or any(not isinstance(v, (int, float)) for v in prices.values()):
        return 0.0
    
    # Set up optional ingredients list
    if optionals is None:
        optionals = []
    if not isinstance(optionals, list) or any(not isinstance(i, str) for i in optionals):
        optionals = []  # Reset if invalid format
    
    # Validate ingredient amounts
    if any(not isinstance(v, (int, float)) or v < 0 for v in kwargs.values()):
        return 0.0

    total_price = 0.0
    for ingredient, amount in kwargs.items():
        try:
            # Only calculate if ingredient is in prices and not optional
            if ingredient in prices and ingredient not in optionals:
                # Divide by 100 since amounts are in cents?
                total_price += prices[ingredient] * amount / 100  
        except (TypeError, KeyError):
            continue  # Skip any problematic ingredients
    
    return total_price

if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))  
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))  
    print(piece_of_cake({}))  