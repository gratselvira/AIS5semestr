# шифр Цезаря

# Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн, жг еютзм ъгб
# Съешь же ещё этих мягких французских булок, да выпей чаю

cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cyrillic_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
encoded_message = 'Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн, жг еютзм ъгб'
print('\nЗакодированное сообщение: "' + encoded_message + '"')
n = 0
input_key = 0
decoded_message = ''

with open('key.txt', 'r') as key_file:
    stored_key = int(key_file.read())

while input_key != stored_key:
    input_key = int(input("Введите ключ: "))
    print("Ключ неверный, попробуйсте снова.")
    n += 1

    if input_key == stored_key:
        print("Ключ верный, декодированное сообщение:")
        for char in encoded_message:
            if char in ' !,.:' :
                decoded_message += char
            elif 'А' <= char <= 'Я':
                decoded_message += cyrillic_upper[(cyrillic_upper.index(char) - stored_key) % len(cyrillic_upper)]
            else:
                decoded_message += cyrillic_lower[(cyrillic_lower.index(char) - stored_key) % len(cyrillic_lower)]

print(decoded_message)
print("Количество попыток: ", n)



















#
# cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# cyrillic_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# shift_key = 0
#
# while shift_key == 0:
#     shift_key = int(input("Введите ключ (количество символов, на которое нужно сдвинуть исходный текст), он не может быть равен 0:\n"))
# # message = input()
# encoded_message = ''
# message = "Съешь же ещё этих мягких французских булок, да выпей чаю"
#
# for char in message:
#     if char in ' !,.:' :
#         encoded_message += char
#     elif 'А' <= char <= 'Я':
#         encoded_message += cyrillic_upper[(cyrillic_upper.index(char) + shift_key) % len(cyrillic_upper)]
#     else:
#         encoded_message += cyrillic_lower[(cyrillic_lower.index(char) + shift_key) % len(cyrillic_lower)]
#
# print('\nЗакодированное сообщение: "' + encoded_message + '"')
#
# with open('key.txt', 'w') as key_file:
#     key_file.write(str(shift_key))
#
# n = 0
# input_key = 0
# decoded_message = ''
#
# with open('key.txt', 'r') as key_file:
#     stored_key = int(key_file.read())
#
# while input_key != stored_key:
#     input_key = int(input("Введите ключ: "))
#     n += 1
#
#     if input_key == stored_key:
#         print("Ключ верный, декодированное сообщение:")
#         for char in encoded_message:
#             if char in ' !,.:' :
#                 decoded_message += char
#             elif 'А' <= char <= 'Я':
#                 decoded_message += cyrillic_upper[(cyrillic_upper.index(char) - shift_key) % len(cyrillic_upper)]
#             else:
#                 decoded_message += cyrillic_lower[(cyrillic_lower.index(char) - shift_key) % len(cyrillic_lower)]
#
# print(decoded_message)
# print("Количество попыток: ", n)
