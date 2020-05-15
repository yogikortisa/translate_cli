#!/usr/bin/env python3
# c0de by yogi@kortisa.com 
# @first Install googletrans module with command: pip install googletrans

from googletrans import Translator

translator = Translator()

print('<<< Your fucking sentences here: ')
x = input()

result = translator.translate(x, dest='id')

print('>>> My SMART translaton result here: ')
print(result.text)
