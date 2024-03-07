from datetime import timedelta, datetime, date


def find_next_weekday(d: date, weekday: int) -> date:
    days_diff = weekday - d.weekday()
    if days_diff <= 0:
        days_diff += 7

    return d + timedelta(days=days_diff)


def get_upcoming_birthdays(users=None) -> list:
    if users is None or not isinstance(users, list):
        return []

    item_index = 0
    days = 7
    current_date = datetime.now().date()
    congratulation_list = []

    for index, user in enumerate(users):
        try:
            item_index = index
            user_birthday_date_this_year = (
                (datetime.strptime(user['birthday'], '%Y.%m.%d')).replace(year=current_date.year)
            ).date()

            if user_birthday_date_this_year < current_date:
                user_birthday_date_this_year = user_birthday_date_this_year.replace(year=current_date.year + 1)

            if 0 <= (user_birthday_date_this_year - current_date).days <= days:
                if user_birthday_date_this_year.weekday() >= 5:
                    user_birthday_date_this_year = find_next_weekday(user_birthday_date_this_year, 0)

                congratulation_list.append({
                    'name': user['name'],
                    'birthday': user['birthday'],
                    'congratulation_date': user_birthday_date_this_year.strftime('%Y.%m.%d')
                })

        except (TypeError, ValueError):
            print(f"Value incorrect value in item by {item_index}")
            return []

    return congratulation_list


def main() -> None:
    try:
        users_list = [
            {"name": "John Doe1", "birthday": "1980.03.05"},
            {"name": "John Doe2", "birthday": "1980.03.06"},
            {"name": "John Doe2", "birthday": "1980.03.07"},
            {"name": "John Doe2", "birthday": "1980.03.08"},
            {"name": "John Doe2", "birthday": "1980.03.09"},
            {"name": "John Doe2", "birthday": "1980.03.10"},
            {"name": "John Doe2", "birthday": "1980.03.11"},
            {"name": "John Doe2", "birthday": "1980.03.12"},
            {"name": "John Doe2", "birthday": "1980.03.13"},
        ]

        upcoming_birthdays = get_upcoming_birthdays(users_list)
        print(f"Список привітань на поточному тижні: {upcoming_birthdays}")

    except (NameError, ValueError):
        print('Не вірні вxідні данні')


if __name__ == "__main__":
    main()
