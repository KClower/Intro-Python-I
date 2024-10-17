"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""




import sys
import calendar
from datetime import datetime

def print_calendar():
    # Get today's date
    today = datetime.today()
    current_month = today.month
    current_year = today.year

    # Get arguments from the command line
    args = sys.argv[1:]

    # Check the number of arguments provided
    if len(args) == 0:
        # No arguments, print the current month's calendar
        month = current_month
        year = current_year
    elif len(args) == 1:
        # One argument, assume it's the month for the current year
        try:
            month = int(args[0])
            year = current_year
        except ValueError:
            print("Invalid month. Please enter a valid number for the month.")
            return
    elif len(args) == 2:
        # Two arguments, assume they are month and year
        try:
            month = int(args[0])
            year = int(args[1])
        except ValueError:
            print("Invalid input. Please enter valid numbers for month and year.")
            return
    else:
        # More than two arguments, print a usage statement
        print("Usage: 14_cal.py [month] [year]")
        print(" - If no arguments are provided, the current month's calendar is displayed.")
        print(" - If one argument is provided, it's assumed to be the month for the current year.")
        print(" - If two arguments are provided, they are the month and year.")
        return

    # Print the calendar for the specified month and year
    try:
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatmonth(year, month)
        print(cal_str)
    except calendar.IllegalMonthError:
        print("Invalid month. Please enter a month between 1 and 12.")
    except Exception as e:
        print(f"An error occurred: {e}")

print_calendar()

