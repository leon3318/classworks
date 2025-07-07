# 1
def greet(name, city):
    return f"Привет, {name}! Как погода в {city}?"


print(greet(name="leo", city="spb"))

# 2


def rectangle_area(width, height):
    return width * height


print(rectangle_area(width=2, height=10))

# 3


def join_with_separator(str_1, str_2, separator):
    return str_1 + separator + str_2


print(join_with_separator(str_1="Привет", str_2="Мир", separator="+"))

# 4


def is_in_range(number, min_val, max_val):
    if number >= min_val and number <= max_val:
        return True
    return False


print(is_in_range(number=5, min_val=1, max_val=10))

# 5


def find_in_slice(data, element, start, end):
    if element in data[start:end]:
        return True
    return -1


print(find_in_slice(data=[1, 2, 3, 4, 5, 6], element=6, start=0, end=6))

# 6


def create_user_profile(name, city="Не указан"):
    return f"Имя - {name}, город - {city}"


print(create_user_profile(name="leo"))

# 7


def power(base, exponent=2):
    return base ** exponent


print(power(5))

# 8


def format_header(text, level=2, char="="):
    line = char*len(text)
    header_lines = [line] * level
    return '\n'.join(header_lines) + f"\n{text}\n" + '\n'.join(header_lines)


print(format_header("Здравствуйте!"))

# 9


def create_html_tag(tag, content, style=None, id_name=None):
    tags = ["html", "body", "h1", "h2", "h3", "h4", "h5", "h6", "a",
            "img", "div", "p", "span", "button", "input", "ul", "li"]
    if tag in tags:
        return f"<{tag} style =\"{style}\" id=\"{id_name}\">{content}</{tag}>"
    return f"\"{tag}\" такого тега не существует!"


print(create_html_tag("h10", "Здравствуйте все!"))

# 10


def credit_calc(summ, coef=0.1, duration=5):
    duration *= 12
    payment = round(summ * (coef * (1 + coef) ** duration) /
                    ((1 + coef) ** duration - 1), 2)
    return (f"Ежемесячный платёж по кредиту составляет: {payment} рубля")


print(credit_calc(10000))

# 11


# 12


def find_longest_word(*words):
    longest_strings = "".join(
        [word for word in words if len(word) == len(max(words, key=len))])
    return longest_strings


print(find_longest_word("Привет", "Салют", "Пока"))
