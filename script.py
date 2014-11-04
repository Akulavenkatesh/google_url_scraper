from google import search
from random import randint
from time import sleep
import csv


keywords = ['Vijay Singh Pro Golfer',
'William McGirt	Pro Golfer'
'Rahul Dravid Cricket'
'Sachin Tendulkar Cricket']

for words in keywords:
    a = '\n''%s '%words +"site:en.wikipedia.org/wiki/" '\n'
    print a
    for url in search ( "%s"%a, num=1, start=0, stop=1):
        print url
