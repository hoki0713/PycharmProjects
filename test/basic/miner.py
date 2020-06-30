from dataclasses import dataclass
import re

import nltk
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt


@dataclass
class Model:
    context: str
    fname: str
    target: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def target(self) -> str: return self._target

    @target.setter
    def target(self, target): self._target = target


class Service:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.okt = Okt()
        self.stopwords = []
        self.freqtxt = []

    def extract_token(self, payload):
        print('>> text 문서에서 token 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        print(f'{self.texts[:300]}')


class Controller:
    def __init__(self):
        pass

    def download_dictionary(self):
        nltk.download('all')


def print_menu():
    print('0. Exit\n')
    print('1. 사전 다운로드\n')
    return input('메뉴 선택\n')


app = Controller()
while 1:
    menu = print_menu()
    if menu == '1':
        app.download_dictionary()
    elif menu == '0':
        break