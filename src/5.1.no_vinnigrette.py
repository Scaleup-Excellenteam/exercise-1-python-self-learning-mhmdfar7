# no_vinnigrete.py
import random
import calendar
from datetime import datetime, timedelta

def no_vinnigrete(start_date_str, end_date_str):
    # - This function generates a random date between two input dates
    # - First validates the inputs aren't empty strings
    # - Uses datetime.strptime() which might throw ValueError
    # - Calculates total days between dates for random range
    # - Special Monday check with funny message
    # - Returns formatted date string or error message
    try:
        if not start_date_str or not end_date_str:
            return "Error: Dates cannot be empty."

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        if start_date > end_date:  # Handle reversed dates
            start_date, end_date = end_date, start_date
        
        delta = end_date - start_date
        total_days = delta.days
        
        # Edge case: same start and end date
        if total_days == 0:
            random_date = start_date
        else:
            random_days = random.randint(0, total_days)
            random_date = start_date + timedelta(days=random_days)
        
        # Funny Monday check - keeps the mood light!
        if random_date.weekday() == calendar.MONDAY:
            print("Ain't gettin' no vinaigrette today :(")
        
        return random_date.strftime("%Y-%m-%d")
    
    except ValueError:  # Catch malformed date strings
        return "Error: Please enter valid dates in YYYY-MM-DD format."

if __name__ == '__main__':
    date1 = input("Enter start date (YYYY-MM-DD): ")
    date2 = input("Enter start date (YYYY-MM-DD): ")
    result = no_vinnigrete(date1, date2)
    print(f"Random date: {result}")