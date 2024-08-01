# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести 
# в консоль True, інакше - False. Строку отримати за допомогою функції input()

user_input = input("Введіть рядок: ")

input_set = set(user_input)

if len(input_set) > 10:
    print(True)
else:
    print(False)
