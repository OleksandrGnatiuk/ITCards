from PIL import Image
from datetime import datetime


class Card:

    def __init__(self, name, path_to_pic, side_back: str):
        self.name = name
        self.path_to_pic = path_to_pic
        self.side_back = side_back
        self.cnt_shows = 0
        self.last_show = None
        self.status = 'active'

    def show_front(self):
        img = Image.open(self.path_to_pic)
        img.show()
        return

    def show_back(self):
        return self.side_back


class Topic:

    def __init__(self, name, lst_of_cards=None):
        self.name = name
        if lst_of_cards is None:
            self.lst_of_cards = []
        self.status = 'not_added'

    def add_card(self, card: Card):
        self.lst_of_cards.append(card)

    def __str__(self):
        lst = [card.name for card in self.lst_of_cards]
        result = ", ".join(lst)
        return result


class ITCards:

    def __init__(self):
        self.book = {}

    def add_topic(self, topic: Topic):
        self.book[topic.name] = topic

    def __str__(self):
        result = '\n'
        for name, topic in self.book.items():
            result += f'{name}: {topic}\n'
        return result


py_cards = ITCards()

card_1 = Card("print", r"library/pil.jpg", "Вращаем и сохраняем изображение. \nДля вращения можно использовать функцию rotate, принимающую кол-во градусов.")
card_2 = Card("input", r"library/merge_dict.jpg", "Начиная с Python 3.9, мы наконец-то получили самый элегантный способ объединения словарей - использование операторов объединения.Как показано в примере выше, мы можем просто использовать оператор | для слияния двух разных словарей. Более того, он также поддерживает объединение in-place.")

basic = Topic("basic")
basic.add_card(card_1)
basic.add_card(card_2)

py_cards.add_topic(basic)
# print(pycards)