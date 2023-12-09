# Задание 1
file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

if len(lines1) != len(lines2):
    print("Файлы имеют разное количество строк")
else:
    for i in range(len(lines1)):
        if lines1[i] != lines2[i]:
            print(f"Несовпадающая строка из файла 1: {lines1[i]}")
            print(f"Несовпадающая строка из файла 2: {lines2[i]}")
            break
# Задание 2
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

text = input_file.read()

num_chars = len(text)
num_lines = text.count('\n')
num_vowels = 0
num_consonants = 0
num_digits = 0

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
digits = "0123456789"

for char in text:
    if char in vowels:
        num_vowels += 1
    elif char in consonants:
        num_consonants += 1
    elif char in digits:
        num_digits += 1

output_file.write(f"Количество символов: {num_chars}\n")
output_file.write(f"Количество строк: {num_lines}\n")
output_file.write(f"Количество гласных букв: {num_vowels}\n")
output_file.write(f"Количество согласных букв: {num_consonants}\n")
output_file.write(f"Количество цифр: {num_digits}\n")

input_file.close()
output_file.close()
# Задание 3
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

lines = input_file.readlines()
input_file.close()

if len(lines) > 0:
    del lines[-1]

output_file.writelines(lines)
output_file.close()
# Задание 4
input_file = open('input.txt', 'r')

max_length = 0
for line in input_file:
    line = line.strip()
    if len(line) > max_length:
        max_length = len(line)

input_file.close()

print("Length of the longest line:", max_length)
# Задание 5
word_to_find = input("Enter the word to find: ")

input_file = open('input.txt', 'r')

word_count = 0
for line in input_file:
    words = line.split() 
    for word in words:
        if word == word_to_find:
            word_count += 1

input_file.close()

print(f"The word '{word_to_find}' appears {word_count} times in the file.")
# Задание 6
word_to_find = input("Enter the word to find: ")
word_to_replace = input("Enter the word to replace it with: ")

with open('input.txt', 'r') as file:
    file_data = file.read()

file_data = file_data.replace(word_to_find, word_to_replace)

with open('input.txt', 'w') as file:
    file.write(file_data)

print(f"The word '{word_to_find}' has been replaced with '{word_to_replace}' in the file.")

