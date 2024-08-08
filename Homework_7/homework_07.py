from math import ceil

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multi = 1

    # Complete the while loop condition.
    while True:
        result = number * multi
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number} x {multi} = {result}")

        # Increment the appropriate variable
        multi += 1

multiplication_table(3)
# # Should print:
# # 3x1=3
# # 3x2=6
# # 3x3=9
# # 3x4=12
# # 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

add_two_numbers = lambda num_one, num_two: num_one + num_two

result = add_two_numbers(5, 7)
print(result)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def calculate_average(numbers):
    if not numbers:
        return None  # Повертає None, якщо список порожній
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)
print(average)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

reverse_string = lambda any_string: any_string[::-1]

input_string = "hello"
reversed_string = reverse_string(input_string)
print(reversed_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def find_longest_word(words):
    if not words:
        return None
    longest_word = max(words, key=len)
    return longest_word

words_list = ["apple", "banana", "pineapple", "cherry"]
longest_word = find_longest_word(words_list)
print(longest_word)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

def has_more_than_ten_unique_chars(input_string: str) -> bool:
    """
    Перевіряє, чи рядок містить більше ніж 10 унікальних символів.
    
    :param input_string: Строка, в якій потрібно порахувати унікальні символи.
    :type input_string: str
    :return: True, якщо унікальних символів більше ніж 10, інакше False.
    :rtype: bool
    """
    unique_chars = set(input_string)
    return len(unique_chars) > 10

user_input = input("Введіть рядок: ")
print(has_more_than_ten_unique_chars(user_input))

# task 8

def total_sea_area(black_sea_area: float, azov_sea_area: float) -> float:
    """
    Обчислює загальну площу Чорного і Азовського морів.
    
    :param black_sea_area: Площа Чорного моря в км².
    :type black_sea_area: float
    :param azov_sea_area: Площа Азовського моря в км².
    :type azov_sea_area: float
    :return: Загальна площа обох морів.
    :rtype: float
    """
    return black_sea_area + azov_sea_area

black_sea_area = 436402
azov_sea_area = 37800
print(f"Загальна площа морів: {total_sea_area(black_sea_area, azov_sea_area)} км²")

# task 9

def pages_needed(total_photos: int, photos_per_page: int) -> int:
    """
    Обчислює, скільки сторінок знадобиться для розміщення всіх фотографій.
    
    :param total_photos: Загальна кількість фотографій.
    :type total_photos: int
    :param photos_per_page: Кількість фотографій на одній сторінці.
    :type photos_per_page: int
    :return: Кількість сторінок, необхідних для всіх фотографій.
    :rtype: int
    """
    return ceil(total_photos / photos_per_page)

total_photos = 232
photos_per_page = 8
print(f"Знадобиться {pages_needed(total_photos, photos_per_page)} сторінок.")

# task 10

def fuel_and_refills_needed(distance_km: float, fuel_per_100_km: float, tank_capacity: float) -> tuple[int, int]:
    """
    Обчислює, скільки літрів пального знадобиться для подорожі і скілька разів потрібно заправлятися.
    
    :param distance_km: Відстань подорожі в км.
    :type distance_km: float
    :param fuel_per_100_km: Витрати пального на 100 км.
    :type fuel_per_100_km: float
    :param tank_capacity: Місткість баку в літрах.
    :type tank_capacity: float
    :return: Кількість літрів пального і кількість необхідних заправок.
    :rtype: tuple[int, int]
    """
    fuel_needed = (distance_km / 100) * fuel_per_100_km
    num_refills = ceil(fuel_needed / tank_capacity)
    return int(fuel_needed), int(num_refills)


distance_km = 1600
fuel_per_100_km = 9
tank_capacity = 48
fuel_needed, refills_needed = fuel_and_refills_needed(distance_km, fuel_per_100_km, tank_capacity)
print(f"Для подорожі знадобиться {fuel_needed} літрів бензину.")
print(f"Необхідно заїхати на заправку щонайменше {refills_needed} разів.")

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
