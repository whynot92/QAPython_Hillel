# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

print(f'Яблук: {apples}')
print(f'Бананів: {banana}')

# task 05 == виправте назви змінних
_storona = 1    # Не виправив так як змінні можуть починатимь з "_"
storona_2 = 2
storona_3 = 3   # Ми можемо використовувати кирилицю в змінних, але я змінив 
# тому-що в проф. проектах може призвести до помилки кодування та в складності
# розуміння інших розробників
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача

perimetery = _storona + storona_2 + storona_3 + storona_4

print(f'Периметр дорівнює: {perimetery}')

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 07
# """
# У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?
# """
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2

sum_trees = apple_trees + pear_trees + plum_trees

print(f'Всього у нас {sum_trees} дерев у садку.')


# task 08
# """
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?
# """

before_lunch = 5
after_lunch = before_lunch - 10
evening = after_lunch + 4

print(f'На вечір {evening} °C')

# task 09
# """
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?
# """

all_boys = 24
all_girls = 24 / 2
boys_sick = 1
did_not_come = 2

all_kids_today = (all_boys + all_girls) - (boys_sick + did_not_come)

print(f'Сьогодні в гуртку: {int(all_kids_today)} дітей.')

# task 10
# """
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
# """

first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2

all_price = first_book + second_book + third_book

print(f'Загальна вартість усіх книг якщо купити по одному примірнику: \
{int(all_price)} грн.')
