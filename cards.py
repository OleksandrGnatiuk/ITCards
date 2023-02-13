from datetime import datetime
import pickle
from PIL import Image


class Card:

    def __init__(self, name, path_to_pic, side_back: str):
        self.name = name
        self.path_to_pic = path_to_pic
        self.side_back = side_back
        self.cnt_shows = 0
        self.last_show = datetime.now()
        self.status = 'active'

    def show_front(self):
        img = Image.open(self.path_to_pic)
        img.show()
        return

    def show_back(self):
        return self.side_back

    def __str__(self):
        return f"{self.name}: \n{self.show_back()} \nКількість показів: {self.cnt_shows}\nОстанній показ: {self.last_show}\n{self.status}"


class Topic:

    def __init__(self, name, lst_of_cards=None):
        self.name = name
        if lst_of_cards is None:
            self.lst_of_cards = []
        self.status = "new"

    def add_card(self, card: Card):
        self.lst_of_cards.append(card)

    def __str__(self):
        lst = [card.name for card in self.lst_of_cards]
        result = ", ".join(lst)
        return f"{result}\nStatus: {self.status}"


class ITCards:

    def __init__(self):
        self.book = {}
        self.read_from_file()

    def add_topic(self, topic: Topic):
        self.book[topic.name] = topic
        self.save_to_file()

    def __str__(self):
        result = '\n'
        for name, topic in self.book.items():
            result += f'\n{name}: {topic}\n'
        return result

    def save_to_file(self):
        with open('cards.pickle', 'wb') as fd:
            pickle.dump(self.book, fd)

    def read_from_file(self):
        try:
            with open('cards.pickle', 'rb') as fd:
                self.book = pickle.load(fd)
        except FileNotFoundError:
            self.book = {}


py_cards = ITCards()
