# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод
#
# 8-5+2-1
# Вывод
# 4
"""
math_exp = input("Введите выражение: ")

res = int(math_exp[0])
operations = [op for op in math_exp[1::2]]
nums = [int(n) for n in math_exp[2::2]]

for i in range(len(nums)):
    if operations[i] == "+":
        res += nums[i]
    else:
        res -= nums[i]

print(f"Результат: {res}")
"""

# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

"""
full_str = input("Введите строку: ")
word = ""
for ch in full_str:
    if ch == " ":
        print(word)
        word = ""
    else:
        word += ch
if word != "":
    print(word)
"""