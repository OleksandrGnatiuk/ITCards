from random import sample
from cards import pycards


def main():
    while True:
        for name in pycards.book:
            if pycards.book[name].status == 'active':
                active_card = sample(pycards.book[name].lst_of_cards, 1)
                break
            else:
                active_card = sample(pycards.book["basic"].lst_of_cards, 1)
                break
        print(active_card[0].show_front())
        a = input("\nПодивитися пояснення. y / n: \n")
        if a.lower().strip() == "y":
            print(active_card[0].show_back())

        b = input("Чи зрозумілий приклад? y / n: \n")
        if b.lower().strip() == "y":
            active_card[0].score += 1

if __name__ == "__main__":
    main()