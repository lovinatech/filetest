# Читаем предыдущий ответ из файла
with open("answers.txt", "r") as file:
    # Читаем все строки из файла в список
    lines = file.readlines()

# Если список не пустой, то последняя строка будет предыдущим ответом
if lines:
    previous_answer = lines[-1].strip()
    print("Предыдущий ответ:", previous_answer)

# Получаем новый ответ от пользователя
new_answer = "sraka"

# Открываем файл для записи нового ответа
with open("answers.txt", "w") as file:
    # Записываем новый ответ в файл
    file.write(new_answer + "\n")

# Выводим сообщение об успешной записи нового ответа в файл
print("Новый ответ успешно сохранен в файле!")
