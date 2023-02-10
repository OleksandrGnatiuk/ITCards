from cards import py_cards, Topic, Card
from datetime import datetime, timedelta


def create_active_list(lst: list[Topic]) -> list:
    active_list = []
    for topic in lst:
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


def status_of_card(card: Card):
    interval = card.last_show - datetime.now()
    if card.cnt_shows == 0:
        card.cnt_shows = "active"
    elif card.cnt_shows == 1 and interval >= timedelta(minutes=25):
        card.cnt_shows = "active"
    elif card.cnt_shows == 2 and interval >= timedelta(hours=8):
        card.cnt_shows = "active"
    elif card.cnt_shows == 3 and interval >= timedelta(days=1):
        card.cnt_shows = "active"
    elif card.cnt_shows == 4 and interval >= timedelta(days=3):
        card.cnt_shows = "active"
    elif card.cnt_shows == 5 and interval >= timedelta(days=10):
        card.cnt_shows = "active"
    elif card.cnt_shows == 6 and interval >= timedelta(days=30):
        card.cnt_shows = "active"
    elif card.cnt_shows == 7 and interval >= timedelta(days=90):
        card.cnt_shows = "active"
    else:
        card.last_show = "non active"


if __name__ == "__main__":
    create_active_list(py_cards.book)
