import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import requests
import urllib3
import socket
from datetime import datetime
import time

from header import *



user_instr = []
user_alarm = []
user_get_alarm = []
user_wake = []

while True:
    try:
        session = requests.Session()

        vk_session = vk_api.VkApi(token=token)
        longpoll = VkLongPoll(vk_session)
        vk = vk_session.get_api()
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
           #Слушаем longpoll, если пришло сообщение то:
                #if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
                    if event.from_user: #Если написали в ЛС
                        if event.text !='/alarm':
                            if event.user_id not in user_instr and event.user_id not in user_alarm:
                                vk.messages.send(  # Отправляем сообщение
                                    user_id=event.user_id,
                                    message=Hello_message,
                                    random_id=get_random_id()
                                )
                                user_instr.append(event.user_id)
                            if event.user_id not in user_get_alarm and event.user_id in user_alarm and event.text !='/wake':
                                vk.messages.send(  # Отправляем сообщение
                                    user_id=event.user_id,
                                    message='Ваше сообщение обязательно будет доставлено создателю!',
                                    random_id=get_random_id()
                                )
                                user_get_alarm.append(event.user_id)
                        if event.text == '/alarm':
                            if event.user_id not in user_alarm :
                                vk.messages.send(  # Отправляем сообщение
                                    user_id=event.user_id,
                                    message='Я вас внимательно слушаю.',
                                    random_id=get_random_id()
                                )
                                user_alarm.append(event.user_id)
                        if event.text == '/wake':
                            if event.user_id not in user_get_alarm and event.user_id in user_alarm:
                                vk.messages.send(  # Отправляем сообщение
                                    user_id=event.user_id,
                                    message='Сначала введите ваше важное собщение для создателя!',
                                    random_id=get_random_id()
                                )

                            elif event.user_id not in user_wake:
                                vk.messages.send(  # Отправляем сообщение
                                    user_id=event.user_id,
                                    message='Я попробую разбудить создателя.\nНо ничего не обещаю...',
                                    random_id=get_random_id()
                                )
                                user_wake.append(event.user_id)
    except (requests.exceptions.ReadTimeout, socket.timeout, urllib3.exceptions.ReadTimeoutError):
        time.sleep(1)
        print(datetime.now().time())


