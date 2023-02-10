from cards import py_cards, Topic, Card
from datetime import datetime, timedelta


def create_active_list(dct) -> list[Card]:
    active_list: list[Card] = []
    for topic in dct.values():
        if topic.status == "new":
            active_list.extend(topic.lst_of_cards)
            topic.status = "added"
        elif topic.status == "added":
            for card in topic.lst_of_cards:
                status_of_card(card)
                if card.status == "active":
                    active_list.append(card)
        else:
            continue
    return active_list


intervals = {
    1: timedelta(minutes=25),
    2: timedelta(hours=8),
    3: timedelta(days=1),
    4: timedelta(days=3),
    5: timedelta(days=10),
    6: timedelta(days=30),
    7: timedelta(days=90)
}


def status_of_card(card: Card):
    if card.cnt_shows == 0:
        card.cnt_shows = "active"
    else:
        interval = card.last_show - datetime.now()
        for key, value in intervals.items():
            if card.cnt_shows == key and interval >= value:
                card.cnt_shows = "active"
            else:
                card.last_show = "non active"


if __name__ == "__main__":
    create_active_list(py_cards.book)
