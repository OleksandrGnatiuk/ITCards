
class Card:

    def __init__(self, name, side_front, side_back: str):
        self.name = name
        self.side_front = side_front
        self.side_back = side_back
        self.score = 0

    def show_front(self):
        return self.side_front

    def show_back(self):
        return self.side_back

    def i_know(self):
        self.score += 1


class Topic:

    def __init__(self, name, lst_of_cards=None):
        self.name = name
        if lst_of_cards is None:
            self.lst_of_cards = []
        self.status = 'in_future'

    def add_card(self, card: Card):
        self.lst_of_cards.append(card)


    def __str__(self):
        lst = [card.name for card in self.lst_of_cards]
        result = ", ".join(lst)
        return result



class PyCards:

    def __init__(self):
        self.book = {}

    def add_topic(self, topic: Topic):
        self.book[topic.name] = topic

    def __str__(self):
        result = '\n'
        for name, topic in self.book.items():
            result += f'{name}: {topic}\n'
        return result



pycards = PyCards()


card_1 = Card("print", "\nметод print('Hello. World')", "Функція для виводу результату на екран. Містить параметри за замовчуванням 'sep=' та 'end='")
card_2 = Card("input", "\nметод input()", "Функція для вводу даних з клавіатури")

basic = Topic("basic")
basic.add_card(card_1)
basic.add_card(card_2)

pycards.add_topic(basic)
# print(pycards)