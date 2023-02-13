from cards import py_cards, Card
from datetime import datetime, timedelta


def create_active_list(dct) -> list[Card]:
    active_list: list[Card] = []
    for topic in dct.values():
        if topic.status == "new":
            active_list.extend(topic.lst_of_cards)
            topic.status = "added"
        elif topic.status == "added":
            for card in topic.lst_of_cards:
                check_status_of_card(card)
                if card.status == "active":
                    active_list.append(card)
        else:
            continue
    return active_list

# Формуємо часові інтервали показу карток, в залежності від кількості їх попередніх показів
intervals = {
    1: timedelta(minutes=1),
    2: timedelta(minutes=2),
    3: timedelta(minutes=10),
    4: timedelta(hours=1),
    5: timedelta(hours=5),
    6: timedelta(days=1),
    7: timedelta(days=5),
    8: timedelta(days=25),
    9: timedelta(days=120),
    10: timedelta(days=730)
}


def check_status_of_card(card: Card):
    time = datetime.now() - card.last_show
    if card.cnt_shows == 0:
        card.status = "active"
    elif card.cnt_shows > 10 and time >= timedelta(days=90):
        card.status = "active"
    else:
        for cnt, interval in intervals.items():
            if card.cnt_shows == cnt and time >= interval:
                card.status = "active"
                break
            else:
                card.status = "non active"


if __name__ == "__main__":
    create_active_list(py_cards.book)
