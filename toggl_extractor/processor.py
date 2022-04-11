from datetime import date, timedelta
from toggl_extractor import slack_client
from toggl_extractor import toggl_client

YESTERDAY = date.today() - timedelta(1)


def get_workdays_for_users_per_day(range, slack=False):
    start_date = calculate_start_date_from_range(range)

    raw_time_entries = toggl_client.get_time_entries(start_date, YESTERDAY)
    structured_entries = structure_raw_entries_by_day_and_user(raw_time_entries)
    workdays = calculate_workdays_for_users_per_day(structured_entries)
    message = convert_dict_of_dicts_to_string(workdays)

    if slack:
        try:
            slack_client.post_to_slack(message)
        except:
            return slack_client.post_to_slack(message)
    else:
        return message


def get_efficiency_percentage_per_user_per_day(range, slack=False):
    start_date = calculate_start_date_from_range(range)

    raw_time_entries = toggl_client.get_time_entries(start_date, YESTERDAY)
    structured_entries = structure_raw_entries_by_day_and_user(raw_time_entries)
    effective_times = effective_worktime_calculator(structured_entries)
    workdays = calculate_workdays_for_users_per_day(structured_entries)
    calculated_efficiency_per_user_per_day = (
        calculate_efficiency_percentage_per_user_per_day(effective_times, workdays)
    )
    message = convert_dict_of_dicts_to_string(calculated_efficiency_per_user_per_day)
    if slack:
        try:
            slack_client.post_to_slack(message)
        except:
            return slack_client.post_to_slack(message)
    else:
        return message


def get_average_efficiency_per_user_in_range(range, slack=False):
    start_date = calculate_start_date_from_range(range)

    raw_time_entries = toggl_client.get_time_entries(start_date, YESTERDAY)
    structured_entries = structure_raw_entries_by_day_and_user(raw_time_entries)
    effective_times = effective_worktime_calculator(structured_entries)
    workdays = calculate_workdays_for_users_per_day(structured_entries)
    calculated_efficiency_per_user_per_day = (
        calculate_efficiency_percentage_per_user_per_day(effective_times, workdays)
    )
    average_efficiency_per_user_in_range = (
        calculate_average_efficiency_per_user_in_range(
            calculated_efficiency_per_user_per_day
        )
    )
    message = convert_dict_of_dicts_to_string(average_efficiency_per_user_in_range)

    if slack:
        try:
            slack_client.post_to_slack(message)
        except:
            return slack_client.post_to_slack(message)
    else:
        return message


def get_efficiency_of_set_user_per_day(range, set_user, slack=False):
    start_date = calculate_start_date_from_range(range)

    raw_time_entries = toggl_client.get_time_entries(start_date, YESTERDAY)
    structured_entries = structure_raw_entries_by_day_and_user(raw_time_entries)
    effective_times = effective_worktime_calculator(structured_entries)
    workdays = calculate_workdays_for_users_per_day(structured_entries)
    calculated_efficiency_per_user_per_day = (
        calculate_efficiency_percentage_per_user_per_day(effective_times, workdays)
    )
    calculated_efficiency_of_set_user_per_day = (
        calculate_efficiency_of_set_user_per_day(
            calculated_efficiency_per_user_per_day, set_user
        )
    )
    message = convert_dict_of_dicts_to_string(calculated_efficiency_of_set_user_per_day)
    if slack:
        try:
            slack_client.post_to_slack(message)
        except:
            return slack_client.post_to_slack(message)
    else:
        return message


def calculate_efficiency_of_set_user_per_day(efficiency_per_user_per_day, set_person):
    extracted_efficiency_of_set_user_per_day = {}
    the_one_and_only_key = str(f"The daily efficiencies of {set_person} are")
    extracted_efficiency_of_set_user_per_day[the_one_and_only_key] = {}
    for date in efficiency_per_user_per_day:
        for user in efficiency_per_user_per_day[date]:
            first_name = extract_first_name(user)
            if first_name == set_person or user == set_person:
                extracted_efficiency_of_set_user_per_day[the_one_and_only_key][
                    date
                ] = efficiency_per_user_per_day[date][user]

    return extracted_efficiency_of_set_user_per_day


def extract_first_name(full_name):
    first_name = str()
    for char in full_name:
        if char is not " ":
            first_name = first_name + char
        else:
            break
    return first_name


def calculate_average_efficiency_per_user_in_range(
    calculated_efficiency_per_user_per_day,
):
    first_date = extract_last_key_in_dict(calculated_efficiency_per_user_per_day)
    last_date = extract_first_key_in_dict(calculated_efficiency_per_user_per_day)
    the_one_and_only_key = str(
        f"The efficiencies of all the users between {first_date} and {last_date} are"
    )
    average_efficiency_per_user_in_range = {}
    average_efficiency_per_user_in_range[the_one_and_only_key] = {}
    users_and_efficiencies = {}

    for day in calculated_efficiency_per_user_per_day:
        for user in calculated_efficiency_per_user_per_day[day]:
            if user in users_and_efficiencies:
                users_and_efficiencies[user].insert(
                    0, calculated_efficiency_per_user_per_day[day][user]
                )
            else:
                users_and_efficiencies[user] = [
                    calculated_efficiency_per_user_per_day[day][user]
                ]
    for user in users_and_efficiencies:
        average_efficiency_per_user_in_range[the_one_and_only_key][
            user
        ] = average_of_strings_in_list(users_and_efficiencies[user])

    return average_efficiency_per_user_in_range


def average_of_strings_in_list(list_of_string_percentages):
    running_sum = 0
    for item in list_of_string_percentages:
        running_sum = running_sum + convert_string_percentage_to_int(item)
    average = running_sum / len(list_of_string_percentages)
    return str(round(average)) + " %"


def convert_string_percentage_to_int(string_percetange):
    return int(string_percetange[0:-2])


def extract_last_key_in_dict(dict):
    return list(dict.keys())[len(dict) - 1]


def extract_first_key_in_dict(dict):
    return list(dict.keys())[0]


def calculate_workdays_for_users_per_day(structured_entries):
    calculated_workdays_for_each_employee = {}
    for day in structured_entries:
        calculated_workdays_for_each_employee[day] = {}
        for employee in structured_entries[day]:
            list = structured_entries[day][employee]
            start_of_the_day = convert_time_string_to_float(list[0][0])
            end_of_the_day = convert_time_string_to_float(list[len(list) - 1][1])
            gap = calculate_gaps_in_the_workday_bigger_than_30mins(list)
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
            calculated_workdays_for_each_employee[day][employee] = str(workday) + " h"
    return calculated_workdays_for_each_employee


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


def calculate_start_date_from_range(range):
    """
    takes the time range (number of days) and returns 2 dates start date (present day-time range = start date)
    and the present day, both in a YYYY-MM-DD format
    """
    return date.today() - timedelta(int(range))


def extract_date_from_string(iso_date_time):
    return iso_date_time[0:10]


def extract_time_from_string(iso_date_time):
    return iso_date_time[11:16]


def convert_time_string_to_float(iso_date_time):
    """divide minutes by 60 to convert them into hours, finally getting a float like
    5.6 hours return hours + minutes / 60"""
    hours = int(iso_date_time[0:2])
    minutes = +(int(iso_date_time[3:5]) / 60)

    return hours + minutes


def calculate_gaps_in_the_workday_bigger_than_30mins(entries_list_per_pers_day):
    """takes a entries_list_per_pers_day of entries an employee submitted in a day and returns
    the sum of the breaks which are higher than 30 mins. If there are no such breaks,
    then it returns 0"""
    final_calculated_gap = 0.0
    for i in range(len(entries_list_per_pers_day) - 1):
        between_entries_gap_start = convert_time_string_to_float(
            entries_list_per_pers_day[i][1]
        )
        between_entries_gap_end = convert_time_string_to_float(
            entries_list_per_pers_day[i + 1][0]
        )
        if between_entries_gap_end - between_entries_gap_start > 0.5:
            final_calculated_gap = final_calculated_gap + (
                between_entries_gap_end - between_entries_gap_start
            )
    if final_calculated_gap > 0.5:
        return final_calculated_gap - 0.5
    else:
        return final_calculated_gap


def calculate_efficiency_percentage_per_user_per_day(effective_times, workdays):
    efficiency_per_person_per_day = {}
    for day in effective_times:
        for person in effective_times[day]:
            effective_time_string = effective_times[day][person]
            workday_string = workdays[day][person]
            expected_time_plus_break = float(effective_time_string[0:4]) * 116
            efficiency_percentage = expected_time_plus_break / float(
                workday_string[0:4]
            )
            if day in efficiency_per_person_per_day:
                efficiency_per_person_per_day[day][person] = (
                    str(round(efficiency_percentage)) + " %"
                )

            else:
                efficiency_per_person_per_day[day] = {
                    person: str(round(efficiency_percentage)) + " %"
                }
    return efficiency_per_person_per_day


def effective_worktime_calculator(structured_entries):
    effective_worked_times_per_user_per_day = {}
    for day in structured_entries:
        effective_worked_times_per_user_per_day[day] = {}
        for person in structured_entries[day]:
            list = structured_entries[day][person]
            effective_time_worked = float()
            for entry in list:
                entry_start = convert_time_string_to_float(entry[0])
                entry_stop = convert_time_string_to_float(entry[1])
                if entry_start <= entry_stop:
                    effective_time_worked = (
                        effective_time_worked + entry_stop - entry_start
                    )

                else:
                    effective_time_worked = (
                        effective_time_worked + float(24) - entry_start + entry_stop
                    )

            if effective_time_worked < 10.0:
                effective_worked_times_per_user_per_day[day][person] = (
                    "0" + str(round(effective_time_worked, 2)) + " h"
                )

                """this will add a zero in front of a number to transform 4.1 in 04.1"""
            else:
                effective_worked_times_per_user_per_day[day][person] = (
                    str(round(effective_time_worked, 2)) + " h"
                )

                """this will NOT add a zero in front of a number beacuse it already has both units and tens eg. 12.4"""
    return effective_worked_times_per_user_per_day


def convert_dict_of_dicts_to_string(result):
    converted_dict_of_dicts_to_string = str()
    for day in result:
        converted_dict_of_dicts_to_string = converted_dict_of_dicts_to_string + str(
            day + ":" + "\n"
        )
        for person in result[day]:
            converted_dict_of_dicts_to_string = converted_dict_of_dicts_to_string + str(
                person + ": " + result[day][person] + "\n"
            )
        converted_dict_of_dicts_to_string = converted_dict_of_dicts_to_string + str(
            "\n\n"
        )
    return converted_dict_of_dicts_to_string
