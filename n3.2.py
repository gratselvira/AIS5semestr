import random
import string

characters = [random.choice(string.ascii_letters) for _ in range(20)] #ascii_letters - все латинские буквы в виде строки, рандом выбирает оттуда
print("Сгенерированный список символов:", characters)
lowercase_count = sum(1 for char in characters if 'a' <= char <= 'z')
uppercase_count = sum(1 for char in characters if 'A' <= char <= 'Z')

print(f"Количество строчных букв: {lowercase_count}")
print(f"Количество прописных букв: {uppercase_count}")
