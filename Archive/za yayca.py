note = {}
username = input("введите имя пользователя: ")
title = []
# book = True
while True:  # можно поставить 2 больше 1 или что-нибудь подобное, то что будет правдой
    can = input("\nхотите ввести заголовок да\нет: ")
    if can == "нет":  # ("хотите ввести еще один заголовок (да\нет): " )) == "нет": # введите ещё один заголовок или нет
        break
    elif can == "да":
        title.append(input("введите заголовок заметки: "))
    else:
        print("нераспознанная команда")
        continue
#       note[book] = title
content = input("введите описание заметки: ")
status = input("введите статус заметки: ")
created_date = input("Дата создания заметки (дд.мм.гггг): ")
issue_date = input("дата истечения заметки (дд.мм.гггг): ")
note["имя пользователя"] = username
note["заголовок заметки"] = title
note["описание заметки"] = content
note["микстатус"] = status
note["дата создания заметки"] = created_date[:5]
note["дата истечения заметки"] = issue_date[:5]

for key, value in note.items():
    print(f'\n{key}: {value}')
    # status = []

while True:
    ans = input("хотите обновить статус да/нет ?: ")
    if ans == "нет":
        break
    elif ans == "да":
        print("введите новый статус, где 1 - выполнено, 2 - в процессе, 3 - отложено :")
        while True:
            ank = input()
            if ank == "1":
                note["статус"] = "выполнено"
                break
            elif ank == "2":
                note["статус"] = "в процессе"
                break
            elif ank == "3":
                note["статус"] = " отложено"
                break
            else:
                print("ошибка. Введите корректный ответ.")
        break
note["имя пользователя"] = username
note["заголовок заметки"] = title
note["описание заметки"] = content
# note["введите статус заметки"] = status
note["дата создания заметки"] = created_date[:5]
note["дата истечения заметки"] = issue_date[:5]
for key, value in note.items():
    print(f'\n{key}: {value}')
