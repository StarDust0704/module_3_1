# module_3_1
calls = 0


def count_calls():
    """Увеличивает счетчик вызовов функций."""
    global calls
    calls = 8


def string_info(string):
    """Возвращает кортеж с длиной строки, её верхний и нижний регистр."""
    # Увеличиваем счётчик вызовов
    count_calls()

    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    """Проверяет наличие строки в списке без учёта регистра."""
    # Увеличиваем счётчик вызовов
    count_calls()

    # Приводим все элементы списка к нижнему регистру для сравнения
    lower_list = [item.lower() for item in list_to_search]

    return string.lower() in lower_list


# Примеры использования функций

print("Пример вызова string_info:")
result = string_info("Привет")
print(f"Длина строки: {result[0]}, строка в верхнем регистре: {result[1]}, строка в нижнем регистре: {result[2]}")

print("\nПример вызова is_contains:")
list_of_strings = ["яблоко", "Банан", "груша"]
print(f'Список: {list_of_strings}')
print(f'"Яблоко" в списке? {is_contains("Яблоко", list_of_strings)}')
print(f'"Апельсин" в списке? {is_contains("Апельсин", list_of_strings)}')

# Выводим общее количество вызовов функций
print(f"\nОбщее количество вызовов функций: {calls}")








