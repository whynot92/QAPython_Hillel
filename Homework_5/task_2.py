# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# Додаємо новий запис на початок списку
new_record = ('Jane', 'Doe', 31, 'Scientist', 'San Francisco')
people_records.insert(0, new_record)

print("Список після додавання нового запису:")
print(people_records)

# Обмінюємо елементи з індексами 1 і 5
people_records[1], people_records[5] = people_records[5], people_records[1]

print("\nСписок після обміну елементів з індексами 1 і 5:")
print(people_records)

# Перевіряємо вік людей з індексами 6, 10, 13
indices_to_check = [6, 10, 13]
age_check = True

for index in indices_to_check:
    if people_records[index][2] < 30:
        age_check = False
        break

print("\nВсі люди з індексами 6, 10, 13 мають вік ≥ 30:", age_check)