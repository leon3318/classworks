# 1

ages = [25, 17, 18, 31, 16, 22]
result = []

for age in ages:
    if age >= 18:
        result.append(age)
print(result)

# 2
items = ['камень', 'лягушка', 'вода', 'тыква', 'лягушка']
new_items = []

for item in items:
    if item == "лягушка":
        new_items.append("принц")
    elif item == "тыква":
        new_items.append("карета")
    else:
        new_items.append(item)
print(new_items)

# 3
animals = ['лев', 'зебра', 'тигр', 'жираф', 'волк', 'слон']
predators_counter = 0
herbivores_counter = 0
predators = ['лев', 'тигр', 'волк']

for animal in animals:
    if animal in predators:
        predators_counter += 1
    else:
        herbivores_counter += 1
print(f"Хищников: {predators_counter}, Травоядных: {herbivores_counter}")

4
highs = [100, 110, 105, 120, 125, 130, 128]
the_highest = []
current = []

if len(highs) > 0:
    for i in range(1, len(highs)):
        if highs[i] > highs[i-1]:
            current.append(highs[i])
            if len(current) > len(the_highest):
                the_highest = current.copy()
        else:
            current.clear()

    print(f"Самый длинный непрерывный участок: {the_highest}")
else:
    print("Альпинист не поднимался!")

# 5

dif_lengths = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
main_sum = 0
submain_sum = 0

for item in range(len(dif_lengths)):
    main_sum += dif_lengths[item][item]
    submain_sum += dif_lengths[item][len(dif_lengths)-1-item]
    # submain_sum += dif_lengths[item-1][item-1] Можно ли так решить было?

print(
    f"Сумма главной диагонали: {main_sum}. Сумма побочной диагонали: {submain_sum}.")

# 6

items_2 = [('книга', 800), ('ручка', 50), ('рюкзак', 1500)]
new_items_2 = []


for i in items_2:
    if i[0] == "книга" or i[0] == "ручка":
        new_items_2.append(i[0])
print(new_items_2)

# 7
results = [('Анна', 92), ('Борис', 88), ('Виктор', 95)]
max_res = 0
best_student = ''

for res in results:
    if res[1] > max_res:
        max_res = res[1]
        best_student = res[0]
print(f"Лучший студент - {best_student}")

# 8
workers = [('Иван', 'IT'), ('Мария', 'HR'), ('Петр', 'IT')]
it_team = []
hr_team = []

for worker in workers:
    if worker[1] == "IT":
        it_team.append(worker[0])
    elif worker[1] == "HR":
        hr_team.append(worker[0])
    else:
        pass
print(f"it_team = {it_team},\nhr_team = {hr_team}")


# 9
racer = [('Льюис', 91.5), ('Макс', 91.2), ('Шарль', 92.1)]
sorted_racer = sorted(racer, key=lambda x: x[1])
print(sorted_racer)


# # 10
results = [('Анна', [5, 5, 4]), ('Борис', [4, 3, 5]), ('Виктор', [5, 5, 5])]
dict_results = dict(results)

avg_score = 0
avg = {k: round(sum(v)/len(v), 2) for k, v in dict_results.items()}

inv_dict = {v: k for k, v in avg.items()}

for key, value in inv_dict.items():
    if avg_score < key:
        avg_score = key
print(inv_dict.get(avg_score))

# 11
my_friends = ['Аня', 'Петя', 'Вася']
his_friends = ['Коля', 'Петя', 'Аня']

my_friends_set = set(my_friends)
his_friends_set = set(his_friends)

print(my_friends_set.intersection(his_friends_set))

# 12
unsorted_list = ['Иван', 'Анна', 'Петр', 'Анна', 'Иван']
sorted_list = []

unsorted_set = set(unsorted_list)


# 13

all_tasks = ['помыть посуду', 'погулять']
completed_tasks = ['помыть посуду']

all_tasks_set = set(all_tasks)
completed_tasks_set = set(completed_tasks)
difference_list = list(all_tasks_set.difference(completed_tasks_set))

print(difference_list)

# 14
my_books = {'Война и мир', '1984'}
friend_books = {'1984', 'Мастер и Маргарита'}

my_books_set = set(my_books)
friend_books_set = set(friend_books)

difference_books = my_books_set ^ friend_books_set
print(difference_books)

# # 15
languages = [{'английский', 'испанский'}, {
    'английский', 'французский'}, {'английский', 'немецкий'}]

posol_1 = languages[0]

for language in range(len(languages)):
    union = posol_1 & languages[language]
print(union)

# # 16
names = ['Маша', 'Петя', 'Вася', 'Маша', 'Петя', 'Маша']

dict_names = {name: names.count(name) for name in set(names)}
print(dict_names)

# 17
grades = {'Иванов': 55, 'Петров': 72, 'Сидоров': 48}

for name in grades.keys():
    if grades[name] < 50:
        grades[name] += 5
    elif 50 <= grades[name] < 60:
        grades[name] += 5

print(grades)

# 18
inventory = {'ручка': 20, 'книга': 800, 'рюкзак': 1500}
filtered_inventory = {}

for item, price in inventory.items():
    if price >= 500:
        filtered_inventory[item] = price

print(filtered_inventory)

# 19
capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Италия': 'Рим'}
inverted_capitals = {}

for country, city in capitals.items():
    inverted_capitals[city] = country

print(inverted_capitals)

# 20
data = {'user': {'name': 'Alice', 'profile': {'theme': 'dark'}}}
path = 'user.profile.theme'


keys = path.split('.')

current = data

for key in keys:
    current = current[key]

print(current)
