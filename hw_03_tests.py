import unittest
from datetime import datetime, timedelta

from hw_03_1 import get_days_from_today
from hw_03_2 import get_numbers_ticket
from hw_03_3 import normalize_phone
from hw_03_4 import get_upcoming_birthdays


class TestDays(unittest.TestCase):
    def test_count_days_in_past(self):
        res = get_days_from_today('2024-01-15')
        self.assertGreater(res, 0)

    def test_count_days_in_past_with_spaces(self):
        res = get_days_from_today('     2024-01-15            ')
        self.assertGreater(res, 0)

    def test_count_days_named_parameter(self):
        res = get_days_from_today(date='2024-01-15')
        self.assertGreater(res, 0)

    def test_count_days_named_parameter_short(self):
        res = get_days_from_today(date='2024-1-5')
        self.assertGreater(res, 0)

    def test_count_days_in_future(self):
        res = get_days_from_today('2025-01-15')
        self.assertLess(res, 0)

    def test_count_days_not_date_format(self):
        res = get_days_from_today('20250115')
        self.assertIsNone(res)

    def test_count_days_wrong_value(self):
        res = get_days_from_today('hello world')
        self.assertIsNone(res)

    def test_count_days_without_parameter(self):
        res = get_days_from_today()
        self.assertIsNone(res)


class TestLottery(unittest.TestCase):
    def test_lottery_1_of_49_choose_6(self):
        self.assertTrue(len(get_numbers_ticket(1, 49, 6)))

    def test_lottery_1_of_36_choose_5(self):
        self.assertTrue(len(get_numbers_ticket(1, 36, 5)))

    def test_lottery_1_of_36_choose_5_named_parameter(self):
        self.assertTrue(len(get_numbers_ticket(max_value=36, quantity=5, min_value=1)))

    def test_lottery_1_of_5_choose_5(self):
        self.assertTrue(len(get_numbers_ticket(1, 5, 5)))

    def test_lottery_1_of_5_choose_10(self):
        self.assertTrue(len(get_numbers_ticket(1, 5, 10)) == 0)

    def test_lottery_input_not_valid_parameter(self):
        self.assertTrue(len(get_numbers_ticket('a', 'b', 'c')) == 0)

    def test_lottery_input_without_parameter(self):
        self.assertTrue(len(get_numbers_ticket()))


class TestNormalizePhone(unittest.TestCase):
    def test_normalize_phone_not_valid_parameter(self):
        self.assertEqual(normalize_phone(1), '')

    def test_normalize_phone_not_valid_parameter_string(self):
        self.assertEqual(normalize_phone('hello world'), '')

    def test_normalize_phone_parameter_empty_string(self):
        self.assertEqual(normalize_phone(''), '')

    def test_normalize_phone_phone(self):
        self.assertEqual(normalize_phone(phone_number="    +38(050)123-32-34"), '+380501233234')

    def test_normalize_phone_without_parameter(self):
        self.assertEqual(normalize_phone(), '')


class TestBirthdayList(unittest.TestCase):
    def test_birthday_list_not_valid_parameter(self):
        res = get_upcoming_birthdays(1)
        self.assertEqual(len(res), 0)

    def test_birthday_list_with_empty_list(self):
        self.assertEqual(len(get_upcoming_birthdays([])), 0)

    def test_birthday_list_without_parameter(self):
        self.assertEqual(len(get_upcoming_birthdays()), 0)

    def test_birthday_with_mistake_date(self):
        users_list = [
            {"name": "John Doe1", "birthday": "1980.0302"},
        ]
        self.assertEqual(len(get_upcoming_birthdays(users_list)), 0)

    def test_birthday_list_not_valid_item(self):
        users_list = [
            {"name": "John Doe1", "birthday": 123},
        ]
        self.assertEqual(len(get_upcoming_birthdays(users_list)), 0)

    def test_birthday_list(self):
        current_date = datetime.now().date()
        birthday_date = current_date.strftime('%Y.%m.%d')
        users_list = [
            {"name": "John Doe1", "birthday": birthday_date},
        ]
        res = get_upcoming_birthdays(users_list)

        self.assertEqual(len(res), 1)


if __name__ == '__main__':
    unittest.main()
