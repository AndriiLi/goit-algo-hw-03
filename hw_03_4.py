from datetime import timedelta, datetime


def get_upcoming_birthdays(users=None) -> list:
    if users is None or not isinstance(users, list):
        return []

    if len(users) == 0:
        return []

    saturday = 5
    item_index = 0

    try:

        current_date = datetime.now().date()
        current_weekday = current_date.weekday()

        current_monday = current_date - timedelta(days=current_weekday)
        current_saturday = current_monday + timedelta(days=saturday)

        previous_sunday = current_monday - timedelta(days=1)
        previous_saturday = current_monday - timedelta(days=2)

        congratulation_list = []

        for index, user in enumerate(users):
            item_index = index
            user_birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

            user_birthday_date_this_year = user_birthday_date.replace(year=current_date.year)

            user['age'] = user_birthday_date_this_year.year - user_birthday_date.year

            if current_monday <= user_birthday_date_this_year < current_saturday:
                user['congratulation_date'] = user_birthday_date_this_year.strftime('%Y.%m.%d')
                user['is_moved_from_weekend'] = False
                congratulation_list.append(user)

            if user_birthday_date_this_year == previous_saturday:
                user['congratulation_date'] = (user_birthday_date_this_year + timedelta(days=2)).strftime('%Y.%m.%d')
                user['is_moved_from_weekend'] = True
                congratulation_list.append(user)

            if user_birthday_date_this_year == previous_sunday:
                user['congratulation_date'] = (user_birthday_date_this_year + timedelta(days=1)).strftime('%Y.%m.%d')
                user['is_moved_from_weekend'] = True
                congratulation_list.append(user)

        return congratulation_list
    except (TypeError, ValueError):
        print(f"Value incorrect value in item by {item_index}")
        return []


def main() -> None:
    users_list = [
        {"name": "John Doe1", "birthday": "1980.02.26"},
        {"name": "John Doe2", "birthday": "1980.03.01"},
        {"name": "John Doe3", "birthday": "1980.03.02"},
        {"name": "John Doe3", "birthday": "1980.03.03"},
        {"name": "John Doe3", "birthday": "1980.03.04"},
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users_list)
    print("Список привітань на цьому тижні: ", upcoming_birthdays)


if __name__ == "__main__":
    main()
