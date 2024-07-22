# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland = '''
"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where ——" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
'''

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

words_with_apostrophe = [word for word in alice_in_wonderland.split() if "'" in word]

for word in words_with_apostrophe:
    print(f'Символ "\'" є в такому слові: {word}')

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

azov_sea = 37800
dark_sea = 436402
total_area = azov_sea + dark_sea 

print(f'Загальна площа Чорного і Азовського моря дорівнює {total_area} км²')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375291
goods_on_first_second = 250449
goods_on_second_third = 222950

goods_third = total_goods - goods_on_first_second
goods_second = goods_on_second_third - goods_third
goods_first = goods_on_first_second - goods_second

print(f"Кількість товарів на першому складі: {goods_first}")
print(f"Кількість товарів на другому складі: {goods_second}")
print(f"Кількість товарів на третьому складі: {goods_third}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

due_date = 18
payment_per_month = 1179
full_cost = due_date * payment_per_month

print(f'Повна вартість компьютера дорівнює: {full_cost} грн.')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a_answer = 8019 % 8
b_answer = 9907 % 9
c_answer = 2789 % 5
d_answer = 7248 % 6
e_answer = 7128 % 5
f_answer = 19224 % 9

print(f'Остача від діленя  8019 : 8 = {a_answer}')
print(f'Остача від діленя  9907 : 9 = {b_answer}')
print(f'Остача від діленя  2789 : 5 = {c_answer}')
print(f'Остача від діленя  7248 : 6 = {d_answer}')
print(f'Остача від діленя  7128 : 5 = {e_answer}')
print(f'Остача від діленя 19224 : 9 = {f_answer}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
need_big_pizzas = 4 * 274
need_middle_pizzas = 2 * 218
need_juices = 4 * 35
need_cakes = 1 * 350
need_water = 3 * 21

all_price = need_cakes + need_middle_pizzas + need_juices + need_cakes + need_water

print(f'Іринці потрібно {all_price} грн. для всього замовлення')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

all_photos = 232
photos_on_page = 8

if all_photos % photos_on_page == 0:
    print(f'Ігорю знадобиться {all_photos // 8} сторінок')
else:
    print(f'Ігорю знадобиться {(all_photos // 8) + 1} сторінок')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance_km = 1600
fuel_consumption_per_100_km = 9
tank_capacity = 48

fuel_needed = (distance_km / 100) * fuel_consumption_per_100_km
num_refills = fuel_needed / tank_capacity

print(f"Для подорожі з Харкова в Будапешт знадобиться {int(fuel_needed)} літрів бензину.")
print(f"Родині необхідно буде заїхати на заправку щонайменше {int(num_refills)} разів, кожного разу заправляючи повний бак.")
