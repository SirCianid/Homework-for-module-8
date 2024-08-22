def personal_summ(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError as exc:
            print(f'Ошибка: yекоректный тип данных для подсчета суммы - {num}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_summ, incorrect_data = personal_summ(numbers)
        total_count = len(numbers) - incorrect_data
        return total_summ / total_count
    except ZeroDivisionError:
        if total_count == 0:
            return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
