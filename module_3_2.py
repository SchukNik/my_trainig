def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if '@' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient.endswith('.ru') != True and recipient.endswith('.com') != True\
    and recipient.endswith('.net') != True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender.endswith('.ru') != True and sender.endswith('.com') != True\
    and sender.endswith('.net') != True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')