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

5
matrix = [[1, 2], [3, 4], [5, 6]]

new_matrix = [numb for row in matrix for numb in row]
print(new_matrix)

# 6
fruits = ['apple', 'banana', 'kiwi']

fruits_dict = {value: len(value) for value in fruits}
print(fruits_dict)

# 7
