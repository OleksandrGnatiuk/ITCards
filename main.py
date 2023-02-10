from random import sample
from datetime import datetime
from cards import py_cards, Card


def main():
    while True:
        active_card: list[Card] = []
        for name in py_cards.book:
            if py_cards.book[name].status == 'active':
                active_card = sample(py_cards.book[name].lst_of_cards, 1)
                break
            else:
                active_card = sample(py_cards.book["basic"].lst_of_cards, 1)
                break
        print(active_card[0].show_front())
        active_card[0].last_show = datetime.now()  # після показу змінюємо для картки дату та час останнього показу
        answer = input("\nПодивитися пояснення. y / n: \n")
        if answer.lower().strip() == "y":
            print(active_card[0].show_back())
        else:
            continue
        answer2 = input("\nПодивитися наступну картку. y / n: \n")
        if answer2.lower().strip() == "y":
            continue


if __name__ == "__main__":
    main()
