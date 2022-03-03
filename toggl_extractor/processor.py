from datetime import date, timedelta
import client


def process_entries(time_range):
    entries = extract_entries_from_request(time_range)
    for i in entries:
        print("\n", i, "\n")
        """the print action is used for me to be able to
        understand how to process the data"""


def extract_entries_from_request(time_range):
    """takes a dictionary - api request from toggl with time entries and indexes the important data into another list"""
    start_date = calculate_date(time_range)
    entry_no = 1
    page_no = 1
    all_entries_done = False
    total_entries = None
    received_entries = []

    while all_entries_done == False:
        datas = client.get_detailed_report(start_date, page_no)
        total_entries = datas["total_count"]
        entry = datas["data"]
        for i in entry:
            entry_no += 1
            received_entries.append(i)

        page_no += 1
        if entry_no >= total_entries:
            all_entries_done = True
    print(total_entries)
    return received_entries


def calculate_date(time_range):
    """takes the time range (number of days) and returns 2 dates start date (present day-time range = start date)
    and the present day, both in a YYYY-MM-DD format"""
    start_date = date.today() - timedelta(int(time_range))
    return start_date
