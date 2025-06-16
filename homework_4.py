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

# 4
highs = [100, 110, 105, 120, 125, 130, 128]
highest = []
current = 0
the_highest = 0


# 5

dif_lengths = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
main_sum = 0
submain_sum = 0

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


# 10
pupils = [('Анна', [5, 5, 4]), ('Борис', [4, 3, 5]), ('Виктор', [5, 5, 5])]
best_middle_note = 0


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

# 15


# 16
