adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# ##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# # task 01 == 
# """ Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')

# # task 02 ==
# """ Замініть .... на пробіл
# """

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", ' ')

# # task 03 ==
# """ Зробіть так, щоб у тексті було не більше одного пробілу між словами.
# """

adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())

# # task 04
# """ Виведіть, скількі разів у тексті зустрічається літера "h"
# """
counter = 0

for i in adwentures_of_tom_sawer:
    counter += 1 if i == 'h' else + 0

print(f"В тексте встречаеться 'h' встречаеться {counter} раз.")

# # task 05
# """ Виведіть, скільки слів у тексті починається з Великої літери?
# """

counter = 0

for i in adwentures_of_tom_sawer:
    counter += 1 if i.isupper() else + 0

print(f'{counter} слов в тексте начинаються с большой буквы.')

# # task 06
# """ Виведіть позицію, на якій слово Tom зустрічається вдруге
# """

positions = [pos for pos, word in enumerate(adwentures_of_tom_sawer.split()) if word == "Tom"]

second_position = positions[1] if len(positions) > 1 else None

print(f'"Tom" во второй раз ничинаеться с {second_position + 1} слова')

# # task 07
# """ Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
# Збережіть результат у змінній adwentures_of_tom_sawer_sentences
# """

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print(len(adwentures_of_tom_sawer_sentences))

# # task 08
# """ Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
# Перетворіть рядок у нижній регістр.
# """

print(f'4 предложение: {adwentures_of_tom_sawer_sentences[3]}')


# # task 09 +
# """ Перевірте чи починається якесь речення з "By the time".
# """

where_text = []

for index, sentence in enumerate(adwentures_of_tom_sawer_sentences):
    if sentence.startswith("By the time"):
        where_text.append(str(index))

if len(where_text) > 0:
    print(f'В предложении "By the time" присутствует в {" ".join(where_text)} строке')
else:
    print('В предложениях "By the time" не присутствует.')


# # task 10
# """ Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
# """
len_sentence = len(adwentures_of_tom_sawer_sentences[-1].split(' '))
print(f'Длина последнего предложения составляет: {len_sentence} слов.')