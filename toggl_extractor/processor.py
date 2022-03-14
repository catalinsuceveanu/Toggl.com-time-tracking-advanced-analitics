from datetime import date, timedelta, datetime

from toggl_extractor import client


def get_workdays_for_users_per_day(range):
    start_date = calculate_start_date_from_range(range)
    YESTERDAY = date.today() - timedelta(1)

    time_entries = client.get_time_entries(start_date, YESTERDAY)
    structured_entries = structure_raw_entries_by_day_and_user(time_entries)
    workdays = calculate_workdays_for_users_per_day(structured_entries)

    return workdays


def calculate_start_date_from_range(range):
    """
    takes the time range (number of days) and returns 2 dates start date (present day-time range = start date)
    and the present day, both in a YYYY-MM-DD format
    """
    return date.today() - timedelta(int(range))


def calculate_workdays_for_users_per_day(structured_entries):
    pass


def print_times(time_range):
    all_entries = structure_entries(time_range)
    for day in all_entries:
        print(day + ":")
        for employee in all_entries[day]:
            list = all_entries[day][employee]
            start_of_the_day = convert_time_string_to_float(list[0][0])
            end_of_the_day = convert_time_string_to_float(list[len(list) - 1][1])
            gap = calculate_gaps(list)
            if start_of_the_day < end_of_the_day:
                workday = round(
                    end_of_the_day - start_of_the_day - gap,
                    1,
                )
            else:
                workday = round(
                    24 - start_of_the_day - gap + end_of_the_day,
                    1,
                )
            print(employee + ": " + str(workday) + " h")
        print("\n")


def structure_raw_entries_by_day_and_user(entries):
    structured_data = {}
    for working_entry in entries:
        start_time = extract_time_from_string(working_entry["start"])
        end_time = extract_time_from_string(working_entry["end"])
        date = extract_date_from_string(working_entry["start"])
        working_time = [start_time, end_time]
        user = working_entry["user"]

        if date in structured_data:
            if user in structured_data[date]:
                structured_data[date][user].insert(0, working_time)
            else:
                structured_data[date][user] = [working_time]

        else:
            structured_data[date] = {user: [working_time]}
    return structured_data


def extract_date_from_string(iso_date_time):
    return iso_date_time[0:10]


def extract_time_from_string(iso_date_time):
    return iso_date_time[11:16]


def convert_time_string_to_float(string_time):
    return int(string_time[0:2]) + (int(string_time[3:5]) / 60)


def calculate_gaps(list):
    gap = 0.0
    for i in range(len(list) - 1):
        gap_start = convert_time_string_to_float(list[i][1])
        gap_end = convert_time_string_to_float(list[i + 1][0])
        if gap_end - gap_start > 0.5:
            gap = gap + (gap_end - gap_start)
    if gap > 0.5:
        return gap - 0.5
    else:
        return gap
