from toggl_extractor import processor
import unittest


class testProcessor(unittest.TestCase):
    def test_convert_time_string_to_float(self):
        test_1 = "00:00"
        test_2 = "02:30"
        test_3 = "23:03"

        self.assertEqual(processor.convert_time_string_to_float(test_1), 0.0)
        self.assertEqual(processor.convert_time_string_to_float(test_2), 2.5)
        self.assertEqual(processor.convert_time_string_to_float(test_3), 23.05)

    def test_calculate_gaps_in_the_workday_bigger_than_30mins(self):
        list_1 = [
            ["09:30", "10:15"],
            ["10:38", "11:30"],
            ["13:15", "14:00"],
            ["14:02", "15:17"],
            ["15:18", "17:17"],
        ]
        list_2 = [
            ["09:30", "10:15"],
            ["10:38", "11:30"],
            ["12:00", "14:00"],
            ["14:02", "15:17"],
            ["15:18", "17:17"],
        ]
        list_3 = []
        list_4 = [["09:30", "10:15"]]
        list_5 = [
            ["01:30", "02:15"],
            ["03:16", "04:00"],
            ["07:22", "14:00"],
            ["15:25", "16:00"],
            ["18:00", "17:17"],
        ]
        self.assertEqual(
            processor.calculate_gaps_in_the_workday_bigger_than_30mins(list_1), 1.25
        )
        self.assertEqual(
            processor.calculate_gaps_in_the_workday_bigger_than_30mins(list_2), 0
        )
        self.assertEqual(
            processor.calculate_gaps_in_the_workday_bigger_than_30mins(list_3), 0
        )
        self.assertEqual(
            processor.calculate_gaps_in_the_workday_bigger_than_30mins(list_4), 0
        )
        self.assertEqual(
            processor.calculate_gaps_in_the_workday_bigger_than_30mins(list_5),
            7.299999999999999,
        )

    def test_calculate_workdays_for_users_per_day(self):

        with open(
            "tests/data/calculate_workdays_for_users_per_day_input.json"
        ) as input_file:
            input = eval(input_file.read())

        with open(
            "tests/data/calculate_workdays_for_users_per_day_output.json"
        ) as output_file:
            output = eval(output_file.read())

        self.assertEqual(
            processor.calculate_workdays_for_users_per_day(input),
            output,
        )

    def test_structure_raw_entries_by_day_and_user(self):
        with open(
            "tests/data/structure_raw_entires_by_day_and_user_input.json"
        ) as input_file:
            input = eval(input_file.read())

        with open(
            "tests/data/structure_raw_entires_by_day_and_user_output.json"
        ) as output_file:
            output = eval(output_file.read())

        self.assertEqual(
            processor.structure_raw_entries_by_day_and_user(input),
            output,
        )

    def test_convert_dict_of_dicts_to_string(self):
        with open(
            "tests/data/convert_dict_of_dicts_to_string_input.json"
        ) as input_file:
            input = eval(input_file.read())

        with open(
            "tests/data/convert_dict_of_dicts_to_string_output.json"
        ) as output_file:
            output = eval(output_file.read())

        self.assertEqual(
            processor.convert_dict_of_dicts_to_string(input),
            output,
        )

    def test_effective_worktime_calculator(self):
        with open("tests/data/effective_worktime_calculator_input.json") as input_file:
            input = eval(input_file.read())

        with open(
            "tests/data/effective_worktime_calculator_output.json"
        ) as output_file:
            output = eval(output_file.read())

        self.assertEqual(processor.effective_worktime_calculator(input), output)

    def test_calculate_efficiency_percentage_per_user_per_day(self):
        with open(
            "tests/data/calculate_efficiency_percentage_per_user_per_day_input_effective_times.json"
        ) as effective_times_file:
            effective_times = eval(effective_times_file.read())
        with open(
            "tests/data/calculate_efficiency_percentage_per_user_per_day_input_workdays.json"
        ) as workdays_input_file:
            workdays = eval(workdays_input_file.read())
        with open(
            "tests/data/calculate_efficiency_percentage_per_user_per_day_output.json"
        ) as output_file:
            output = eval(output_file.read())

        self.assertEqual(
            processor.calculate_efficiency_percentage_per_user_per_day(
                effective_times, workdays
            ),
            output,
        )


if __name__ == "__main__":
    unittest.main()
