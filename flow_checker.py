from dateutil.parser import parse
from datetime import date, timedelta
from datetime import datetime

def check_period(start_of_menstrual_circle, average_menstrual_circle_day):
    string_of_start_of_circle = parse(start_of_menstrual_circle).date()
    print(f"Menstruation starts on {string_of_start_of_circle.strftime('%dth %b %Y')}  and it ends on {(string_of_start_of_circle + timedelta(average_menstrual_circle_day)).strftime('%dth %b %Y')} ")
    print(f"Fertile window is from {(string_of_start_of_circle + timedelta(average_menstrual_circle_day-17)).strftime('%dth %b %Y')} to {(string_of_start_of_circle + timedelta(average_menstrual_circle_day-12)).strftime('%dth %b %Y')}")
    print(f"Ovulation occurs on {(string_of_start_of_circle + timedelta(average_menstrual_circle_day-14)).strftime('%dth %b %Y')} and ends 12-24 hours after.")
    return f"Menstruation starts on {string_of_start_of_circle.strftime('%dth %b %Y')} and it ends on {(string_of_start_of_circle + timedelta(average_menstrual_circle_day)).strftime('%dth %b %Y')}, Fertile window is from {(string_of_start_of_circle + timedelta(average_menstrual_circle_day-17)).strftime('%dth %b %Y')} to {(string_of_start_of_circle + timedelta(average_menstrual_circle_day-12)).strftime('%dth %b %Y')}, Ovulation occurs on {(string_of_start_of_circle + timedelta(average_menstrual_circle_day-14)).strftime('%dth %b %Y')} and ends 12 to 24 hours after."

print(check_period("1/7/2024", 30))