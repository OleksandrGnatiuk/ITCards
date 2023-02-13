from random import sample
from datetime import datetime
from cards import py_cards, Card, Topic
from active_list import create_active_list


def main():
    while True:
        active_list = create_active_list(py_cards.book)
        if len(active_list) > 0:
            active_card: list[Card] = sample(active_list, 1)
            print(active_card[0].show_front())
            active_card[0].last_show = datetime.now()  # після показу змінюємо для картки дату та час останнього показу
            active_card[0].cnt_shows += 1
            active_card[0].status = "non active"
            answer = input("\nПодивитися пояснення. y / n: \n")
            if answer.lower().strip() == "y":
                print(active_card[0].show_back())
            else:
                continue
        else:
            print("Немає карток для повторення")
        answer2 = input("\nПодивитися наступну картку. y / n: \n")
        if answer2.lower().strip() == "y":
            continue


if __name__ == "__main__":
    # card_1_back = """Вращаем и сохраняем изображение.
    # Для вращения можно использовать функцию rotate, принимающую кол-во градусов.
    # """
    # card_1 = Card("card 1", r"library/pil.jpg", card_1_back)
    #
    # card_2_back = """Начиная с Python 3.9, мы наконец-то получили самый элегантный способ
    # объединения словарей - использование операторов объединения.
    # Как показано в примере выше, мы можем просто использовать оператор | для слияния двух разных словарей.
    # Более того, он также поддерживает объединение in-place.
    # """
    # card_2 = Card("card 2", r"library/merge_dict.jpg", card_2_back)
    #
    # basic = Topic("basic")
    # basic.add_card(card_1)
    # basic.add_card(card_2)
    #
    # py_cards.add_topic(basic)

    main()
