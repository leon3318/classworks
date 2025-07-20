# 1
emails = ["ivan@gmail.com", "kate@yahoo.com",
          "john@gmail.com", "test@outlook.com"]

email = [mail for mail in emails if mail.endswith("@gmail.com")]
print(email)

# 2
words = ["Hello", "", "Data", "Science", "", "Python"]

sort_words = [word for word in words if len(word) > 0]
print(sort_words)

# 3
limit_num = int(input("Введите число: "))

odd_squares = [numb**2 for numb in range(limit_num + 1) if numb % 2 != 0]
print(odd_squares)

# 4
items = ["42", "100", "abc", "NaN", "7"]

list_numbers = [int(item) for item in items if item.isdigit()]
print(list_numbers)

# 5
matrix = [[1, 2], [3, 4], [5, 6]]

new_matrix = [numb for row in matrix for numb in row]
print(new_matrix)

# 6
fruits = ['apple', 'banana', 'kiwi']

fruits_dict = {value: len(value) for value in fruits}
print(fruits_dict)

# 7
names = ["john", "DOE", "alice", "Bob"]

names_normal = [name.capitalize() for name in names]
print(names_normal)

# 8
unordered_list = ["Hello", "world", "HELLO", "World", "python"]
ordered_list = []
[ordered_list.append(word.lower())
 for word in unordered_list if word.lower() not in ordered_list]
print(ordered_list)

# 9
n = int(input("Введите число: "))
pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
print(pairs)

# 10
generator_of_squares = (numb ** 2 for numb in range(10**6+1))

# 11

# 12
generator_numbers = (numb for numb in range(100) if numb %
                     3 == 0 and numb % 5 == 0)

# 13
text = "This is a demonstration of how generator expressions work in Python"

list_gen = (word for word in text.split() if len(word) > 4)

# 14
grid = ((x, y) for x in range(10) for y in range(10))

# 15
new_matrix = [[0] * 3 for _ in range(3)]
print(new_matrix)

# 16
new_matrix_of_num = [sum(row) for row in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
print(new_matrix_of_num)


# 17
chessdesk = [[(j + i + 1) % 2 for j in range(9)] for i in range(9)]

for i in range(9):
    for j in range(9):
        print(chessdesk[i][j], end=' ')
    print()
