import calendar

def show_calendar():
    
        year = int(input("Enter the year (e.g., 2025): "))
        month = int(input("Enter the month (1-12): "))
    
        if 1 <= month <= 12:
            print("\nHere is the calendar:")
            print(calendar.month(year, m)) 
