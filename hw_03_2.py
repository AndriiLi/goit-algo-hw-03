import random


def get_numbers_ticket(min_value: int = 1, max_value: int = 36, quantity: int = 5) -> list | None:
    try:
        lottery_numbers = []

        if min_value > max_value:
            min_value, max_value = max_value, min_value

        if min_value > 0 and max_value > 0:
            max_value += 1

        if min_value < 0 and min_value < 0:
            max_value = max_value - (-1)

        list_of_numbers = [num for num in range(min_value, max_value)]

        if len(list_of_numbers) < quantity:
            return lottery_numbers

        lottery_numbers = random.sample(list_of_numbers, quantity)
        return sorted(lottery_numbers)
    except (TypeError, ValueError):
        return None


def main() -> None:
    input_min_value = int(input('Введить мінімальна число: '))
    input_max_value = int(input('Введить максимальне число: '))
    input_quantity_value = int(input('Введить кількість цифр лотереї: '))

    print(f"Виграшна серія {get_numbers_ticket(input_min_value, input_max_value, input_quantity_value)}")


if __name__ == "__main__":
    main()
