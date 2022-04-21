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

    def test_calculate_effective_times(self):

        with open("tests/data/calculate_effective_times_input.json") as input_file:
            input = eval(input_file.read())

        with open("tests/data/calculate_effective_times_output.json") as output_file:
            output = eval(output_file.read())

        self.assertEqual(processor.calculate_effective_times(input), output)

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

    def test_calculate_efficiency_of_set_user_per_day(self):
        with open(
            "tests/data/calculate_efficiency_of_set_user_per_day_input.json"
        ) as input_file:
            input = eval(input_file.read())

        with open(
            "tests/data/calculate_efficiency_of_set_user_per_day_output_1.json"
        ) as output_file_1:
            output_1 = eval(output_file_1.read())
        set_user_1 = "Jitesh"
        """This case tests the normal functionality"""

        with open(
            "tests/data/calculate_efficiency_of_set_user_per_day_output_2.json"
        ) as output_file_2:
            output_2 = eval(output_file_2.read())
        set_user_2 = "Davide"
        """in toggl Davide is registered as "Davide Vitelaru", here we check that it still recognizes him"""

        with open(
            "tests/data/calculate_efficiency_of_set_user_per_day_output_3.json"
        ) as output_file_3:
            output_3 = eval(output_file_3.read())
        set_user_3 = "skdjfbfijbfrljefv"
        """there isn't and probably will never be a user with this name, it still shouldn't crash"""

        self.assertEqual(
            processor.calculate_efficiency_of_set_user_per_day(input, set_user_1),
            output_1,
        )
        self.assertEqual(
            processor.calculate_efficiency_of_set_user_per_day(input, set_user_2),
            output_2,
        )
        self.assertEqual(
            processor.calculate_efficiency_of_set_user_per_day(input, set_user_3),
            output_3,
        )

    def test_extract_first_name(self):
        full_name_1 = "Tudor Vladimirescu"
        full_name_2 = "Andrei Tudose Marian"
        full_name_3 = "Gigi"

        first_name_1 = "Tudor"
        first_name_2 = "Andrei"
        first_name_3 = "Gigi"

        self.assertEqual(processor.extract_first_name(full_name_1), first_name_1)
        self.assertEqual(processor.extract_first_name(full_name_2), first_name_2)
        self.assertEqual(processor.extract_first_name(full_name_3), first_name_3)

    def test_calculate_average_efficiency_per_user_in_range(self):
        self.maxDiff = None
        with open(
            "tests/data/calculate_average_efficiency_per_user_in_range_input.json"
        ) as input_file:
            input = eval(input_file.read())
        with open(
            "tests/data/calculate_average_efficiency_per_user_in_range_output.json"
        ) as output_file:
            output = eval(output_file.read())

        self.assertEqual(
            processor.calculate_average_efficiency_per_user_in_range(input), output
        )

    def test_calculate_average_of_string_percentages_in_list(self):
        case_1 = ["100 %", "50 %", "75 %"]
        output_1 = "75 %"
        case_2 = []
        output_2 = "0 %"
        case_3 = ["1 %"]
        output_3 = "1 %"

        self.assertEqual(
            processor.calculate_average_of_string_percentages_in_list(case_1), output_1
        )
        self.assertEqual(
            processor.calculate_average_of_string_percentages_in_list(case_2), output_2
        )
        self.assertEqual(
            processor.calculate_average_of_string_percentages_in_list(case_3), output_3
        )

    def test_convert_string_percentage_to_int(self):
        case_1 = "100 %"
        output_1 = 100
        case_2 = "0 %"
        output_2 = 0
        case_3 = " 1234567 %"
        output_3 = 1234567

        self.assertEqual(processor.convert_string_percentage_to_int(case_1), output_1)
        self.assertEqual(processor.convert_string_percentage_to_int(case_2), output_2)
        self.assertEqual(processor.convert_string_percentage_to_int(case_3), output_3)

    def test_extract_first_name(self):
        case_1 = "Andrei Vasilescu"
        output_1 = "Andrei"
        case_2 = "Marian"
        output_2 = "Marian"
        case_3 = ""
        output_3 = ""

        self.assertEqual(processor.extract_first_name(case_1), output_1)
        self.assertEqual(processor.extract_first_name(case_2), output_2)
        self.assertEqual(processor.extract_first_name(case_3), output_3)

    def test_calculate_average_efficiency_of_set_user_in_range(self):
        set_person = "Matei"
        with open(
            "tests/data/calculate_efficiency_of_set_user_in_range_input_1.json"
        ) as input_file:
            input = eval(input_file.read())
        with open(
            "tests/data/calculate_efficiency_of_set_user_in_range_output_1.json"
        ) as output_file:
            output = eval(output_file.read())

        self.assertEqual(
            processor.calculate_average_efficiency_of_set_user_in_range(
                input, set_person
            ),
            output,
        )


if __name__ == "__main__":
    unittest.main()
