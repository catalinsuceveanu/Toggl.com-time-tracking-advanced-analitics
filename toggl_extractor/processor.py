from toggl_extractor.client import get_time_entries_in_range
import client


def index_data(time_range):
    """takes a list from of toggl time entries and indexes the important data into another list"""
    for i in client.get_time_entries_in_range(dates_calculator(time_range)):
        print(i)


def dates_calculator(time_range):
    """takes the time range (number of days) and returns 2 dates start date (present day-time range = start date)
    and the present day, both in a YYYY-MM-DD format"""
    print("hello")
    return ("2022-02-21", "2022-02-23")
