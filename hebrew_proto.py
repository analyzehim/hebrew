#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, os


hebrew_letters ={
   'Alef': 'א',
   'Bet': 'ּב',
   'Gimel': 'ג',
   'Dalet':'ד',
   'He':'ה',
   'Vav':'ו',
   'Zayin':'ז',
   'Het':'ח',
   'Tet':'ט',
   'Yod':'י',
   'Final Kaf':'ך',
   'Kaf':'כ',
   'Lamed':'ל',
   'Final Mem':'ם',
   'Mem':'מ',
   'Final Nun':'ן',
   'Nun': 'נ',
   'Samekh': 'ס',
   'Ayin': 'ע',
   'Final Pe': 'ף',
   'Pe': 'פ',
   'Final Tsadi': 'ץ',
   'Tsadi': 'צ',
   'Qof': 'ק',
   'Resh': 'ר',
   'Shin': 'ש',
   'Tav': 'ת'
}

# allowed_letters = [   'Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het', 'Tet', 'Yod',
#                       'Final Kaf', 'Kaf', 'Lamed', 'Final Mem', 'Mem', 'Final Nun', 'Nun', 'Samekh',
#                       'Ayin', 'Final Pe', 'Pe', 'Final Tsadi', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

allowed_letters = [   'Alef', 'Gimel', 'Dalet', 'He', 'Yod',
                      'Lamed', 'Final Mem', 'Mem', 'Final Nun', 'Nun', 'Resh', 'Shin', 'Tav']

hebrew_dict = {}

for letter in allowed_letters:
   hebrew_dict[letter] = hebrew_letters[letter]

#print hebrew_dict

def get_letter():
   key = random.choice(list(hebrew_dict))
   return key, hebrew_dict[key]

def get_keyboard():
   sample = random.sample(list(hebrew_dict.items()),4)
   key = sample[0][1]
   key_english = ''
   for english in hebrew_dict:  # for name, age in dictionary.iteritems():  (for Python 2.x)
      if key == hebrew_dict[english]:
         key_english = english


   variables = [[i[0], 'False'] for i in sample]
   random.shuffle(variables)
   for variable in variables:
      if variable[0] == key_english:
         variable[1] = 'Right'
   keyboard = [[{'text': variables[0][0], 'callback_data': variables[0][1]},{'text': variables[1][0], 'callback_data': variables[1][1]}],
               [{'text': variables[2][0], 'callback_data': variables[2][1]},{'text': variables[3][0], 'callback_data': variables[3][1]}]]
   # for letter in variables:
   #   keyboard.append([{'text': letter, 'callback_data': letter},{'text': letter, 'callback_data': letter},])
   return key, keyboard, key_english

#print get_keyboard()

def get_keyboard():
   files_list = os.listdir('words/')
   try:
      files_list.remove('new')
   except:
      pass
   try:
      files_list.remove('.DS_Store')
   except:
      pass
   #print files_list
   sample = random.sample(files_list, 4)
   key = sample[0].split('.')[0]
   sample = [i.split('.')[0] for i in sample]
   random.shuffle(sample)
   print sample
   keyboard = [[{'text': sample[0]}, {'text': sample[1]}],
               [{'text': sample[2]}, {'text': sample[3]}]]
   # for letter in variables:
   #   keyboard.append([{'text': letter, 'callback_data': letter},{'text': letter, 'callback_data': letter},])
   return key, keyboard

#print random.sample(os.listdir('words/'), 4)

