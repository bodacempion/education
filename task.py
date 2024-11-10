# # dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
# #          'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
# #      	'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
# # dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
# #      	'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}
# # dict3 = {}
# # all_key = set(dict1.keys() or dict2.keys())
# # for word in all_key:
# #     dict3[word] = dict1.get(word,0) + dict2.get(word,0)
# # print(dict3)


# # all_chest.append(dict1.keys() + dict2.keys())

# # if all_key in dict1 or dict2:
# #     dicts = dict1.keys + dict2.keys
# # print(dicts)
# # 1. Сделаем сет из ключей словарей
# # 2. Сделаем цикл по сету
# # 3. В цикле складываем значения ключей
# # dict1.get()



# # A = int(input())
# # B = int(input())
# # print((A // B) >= 0)


# people = [
#     {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
#     {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
#     {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
# ]

# # Каждый словарь в списке представляет программиста, где поле "name" представляет имя, а поле 
# # "languages" - список используемых языков программирования. Выведите на консоль из каждого словаря 
# # имя и последний язык программирования, 
# # чтобы получился следуюший консольный вывод:
# # Name:  Tom
# # Last language:  JavaScript
# # Name:  Bob
# # Last language:  C#
# # Name:  Sam
# # Last language:  Java
# # """

# for slovar in people:
#     print(f"Name:  {slovar['name']}. \nLast language:  {slovar['languages'][-1]}")

import datetime
import random
# not_now_time = datetime.time(12,32,00)
# not_now_date = datetime.date(2010,9,9)
# now_date_and_time = datetime.datetime.now().time()

# print(f"время: {not_now_time}, дата: {not_now_date}, время и год в даннгый момент: {now_date_and_time}")

# random_time = datetime.time(random.randint() < 24,random < 61,random <61)


now_date_and_time = datetime.datetime.now()
birthday = datetime.datetime(2010,9,9,00,00,00)
days = (0)

# print(now_date_and_time - birthday)

while birthday <= now_date_and_time:
    birthday += datetime.timedelta(days=1)
    if birthday.weekday() == 5 or birthday.weekday() == 6:
        days += 1
print(days)
