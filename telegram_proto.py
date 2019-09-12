# -*- coding: utf-8 -*-
import requests
import time
import socket
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings()  # Подавление InsecureRequestWarning, с которым я пока ещё не разобрался
ADMIN_ID = 74102915  # My ID

class Telegram:
    def __init__(self):
        self.TOKEN = '294555914:AAHBHZW8sjA3-oPFNZx98G9vesH-ObDBlAQ'
        #self.TOKEN = '357941877:AAGdDwh8APfdfO_voutaE8SBdkbdwzV1GEg' #test
        self.URL = 'https://api.telegram.org/bot'
        self.chat_id = 74102915
        self.offset = 0
        self.host = socket.getfqdn()
        self.Interval = 2
        log_event("Init completed, host: " + str(self.host))

    def get_updates(self):
        data = {'offset': self.offset + 1, 'limit': 5, 'timeout': 0}
        request = requests.post(self.URL + self.TOKEN + '/getUpdates', data=data, verify=False)
        if (not request.status_code == 200) or (not request.json()['ok']):
            return False

        if not request.json()['result']:
            return
        parametersList = []
        for update in request.json()['result']:
            self.offset = update['update_id']

            if 'message' not in update or 'text' not in update['message']:
                continue

            from_id = update['message']['chat']['id']  # Chat ID
            author_id = update['message']['from']['id']  # Creator ID
            message = update['message']['text']
            date = update['message']['date']
            print update
            try:
                name = update['message']['chat']['first_name']
            except:
                name = update['message']['from']['first_name']
            parameters = (name, from_id, message, author_id, date)
            parametersList.append(parameters)
            try:
                log_event('from %s (id%s): "%s" with author: %s; time:%s' % parameters)
            except:
                pass
        return parametersList

    def send_text_with_keyboard(self, chat_id, text, keyboard):
            try:
                log_event('Sending to %s: %s; keyboard: %s' % (chat_id, text, keyboard))  # Logging
            except:
                log_event('Error with LOGGING')
            json_data = {"chat_id": chat_id, "text": text,
                         "reply_markup": {"keyboard": keyboard, "one_time_keyboard": True}}
            request = requests.post(self.URL + self.TOKEN + '/sendMessage', json=json_data)  # HTTP request

            if not request.status_code == 200:  # Check server status
                return False
            return request.json()['ok']  # Check API

    def send_text(self, chat_id, text):
            try:
                log_event('Sending to %s: %s' % (chat_id, text))  # Logging
            except:
                log_event('Error with LOGGING')
            data = {'chat_id': chat_id, 'text': text}  # Request create
            request = requests.post(self.URL + self.TOKEN + '/sendMessage', data=data, verify=False)  # HTTP request

            if not request.status_code == 200:  # Check server status
                return False
            return request.json()['ok']  # Check API

    def send_photo(self, chat_id, imagePath):
        log_event('Sending photo to %s: %s' % (chat_id, imagePath))  # Logging
        data = {'chat_id': chat_id}
        files = {'photo': (imagePath, open(imagePath, "rb"))}
        requests.post(self.URL + self.TOKEN + '/sendPhoto', data=data, files=files, verify=False)
        request = requests.post(self.URL + self.TOKEN + '/sendPhoto', data=data, files=files, verify=False)  # HTTP request
        if not request.status_code == 200:  # Check server status
            return False

        return request.json()['ok']  # Check API

    def ping(self):
            log_event('Sending to %s: %s' % (self.chat_id, 'ping'))
            data = {'chat_id': self.chat_id, 'text': 'ping'}
            requests.post(self.URL + self.TOKEN + '/sendMessage', data=data, verify=False)  # HTTP request


def log_event(text):
        f = open('hebrew_log.txt', 'a')
        event = '%s >> %s' % (time.ctime(), text)
        print event + '\n'
        f.write(event + '\n')
        f.close()
        return