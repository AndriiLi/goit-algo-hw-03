import random


def get_numbers_ticket(min_value: int = 1, max_value: int = 36, quantity: int = 5) -> list:
    try:
        if min_value < 1 or max_value > 1000 or min_value > max_value or quantity < 0:
            return []

        list_of_numbers = list(range(min_value, max_value + 1))
        lottery_numbers = random.sample(list_of_numbers, quantity)

        return sorted(lottery_numbers)

    except (TypeError, ValueError):
        return []


def main() -> None:
    try:
        input_min_value = int(input('Введить мінімальна число: '))
        input_max_value = int(input('Введить максимальне число: '))
        input_quantity_value = int(input('Введить кількість цифр лотереї: '))
        print(f"Виграшна серія {get_numbers_ticket(input_min_value, input_max_value, input_quantity_value)}")
    except ValueError:
        print('Введені данні не вірні')


if __name__ == "__main__":
    main()
