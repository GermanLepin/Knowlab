import requests
from telebot.models import TeleSettings

token = '1693348909:AAGR1SNPFETAjv76_kN3oZ1D6-ETaMrbbig'
chat_id = '-496524610'
text = 'тест 2'


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_one = text[0:text.find('{')]
            part_two = text[text.find('}') + 1:text.rfind('{')]
            part_three = text[text.rfind('}'):-1]

            text_slice = part_one + tg_name + part_two + tg_phone + part_three
        else:
            text_slice = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice,
            })
        except:
            pass

        finally:
            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Сообщение отправлено!')


    else:
        pass


