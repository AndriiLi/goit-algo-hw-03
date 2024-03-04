from datetime import datetime


def get_days_from_today(date: str = "") -> int | None:
    try:
        input_date = datetime.strptime(date.strip(), '%Y-%m-%d')
        current_date = datetime.now()
        return (current_date - input_date).days
    except (TypeError, ValueError):
        return None


def main() -> None:
    user_input_date = input('Введіть дату у форматі РРРР-ММ-ДД: ')
    date_diff = get_days_from_today(user_input_date)

    if date_diff is not None:
        print(f"Кількість днів між заданою датою і поточною датою {date_diff} днів")
    else:
        print("Введіть дату у вірному форматі")


if __name__ == "__main__":
    main()
