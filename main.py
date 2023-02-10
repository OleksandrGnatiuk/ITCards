from random import sample
from datetime import datetime
from cards import py_cards, Card
from active_list import create_active_list


def main():
    while True:
        active_list = create_active_list(py_cards.book)
        active_card: list[Card] = sample(active_list, 1)
        print(active_card[0].show_front())
        active_card[0].last_show = datetime.now()    # після показу змінюємо для картки дату та час останнього показу
        active_card[0].cnt_shows += 1                # після показу змінюємо для картки кількість показів
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
