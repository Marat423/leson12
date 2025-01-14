def send_email(message, recipient, *, sender = "university.help@gmail.com"):  # создаем функцию
    if '@' not in sender and recipient: # проверяем @
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')): # Проверяем окнчание почты получателя
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')): # проверяем окончание почты отправителя
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient: # проверяем не равны ли отправитель и получатель
        print('Нельзя отправить письмо самому себе.')
        return


    if sender == "university.help@gmail.com": # Проверяем отправителя 
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')