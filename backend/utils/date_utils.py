from datetime import date
import calendar

DAY_TO_NAME_MAP = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
    13: "thirteenth",
    14: "fourteenth",
    15: "fifteenth",
    16: "sixteenth",
    17: "seventeenth",
    18: "eighteenth",
    19: "nineteenth",
    20: "twentieth", 
    21: "twenty-first",
    22: "twenty-second",
    23: "twenty-third",
    24: "twenty-fourth",
    25: "twenty-fifth",
    26: "twenty-sixth",
    27: "twenty-seventh",
    28: "twenty-eighth",
    29: "twenty-nineth",
    30: "thirtieth",
    31: "thirty-first"
}

def get_date_suffix(day: int) -> str:
    if 11 <= day <= 13:
        return 'th'
    
    last_digit = day % 10
    return {1: 'st', 2: 'nd', 3:'rd'}.get(last_digit, 'th')

def get_todays_date() -> str: 
    return date.today().strftime("%d/%m/%Y")

# There are many ways to represent a day in a quote, need this to get all of them based on dd/mm/yyyy
def get_perumtations_of_date(date: str) -> tuple[str, str, str, str]:
    day, month, year = date.split('/')
    full_month = calendar.month_name[int(month)]
    abbr_month = calendar.month_abbr[int(month)]
    return (f'{full_month} {DAY_TO_NAME_MAP[int(day)]}', f'{abbr_month} {DAY_TO_NAME_MAP[int(day)]}', f'{full_month} {str(int(day))}{get_date_suffix(int(day))}', f'{abbr_month} {str(int(day))}{get_date_suffix(int(day))}')