from datetime import date, timedelta
import client


def separate_requests_in_entry(time_range):
    """takes a list from of toggl time entries and indexes the important data into another list"""
    for i in client.get_time_entries_in_range(calculate_date(time_range)):
        print(i)


def calculate_date(time_range):
    """takes the time range (number of days) and returns 2 dates start date (present day-time range = start date)
    and the present day, both in a YYYY-MM-DD format"""
    start_date = date.today() - timedelta(int(time_range))
    return start_date
