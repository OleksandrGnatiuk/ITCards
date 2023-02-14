import json

# dict_of_topics = {
#    1: {"Змінні, типи даних": 0},
#    2: {"Рядки та їх методи": 0}, 
#    3: {"Списки та їх методи": 0},
#    4: {"Умови та цикли": 0}, 
#    5: {"Кортежі та їх методи": 0}, 
#    6: {"Словники та їх методи": 0}, 
#    7: {"Множини та їх методи": 0,},
#    8: {"Функції": 0}, 
#    9: {"Форматування рядків": 0}, 
#    10: {"Collections": 0}, 
#    11: {"Regular Expressions": 0},
#    12: {"datetime": 0},
#    13: {"random": 0},
#    14: {"Класи та об'єкти": 0}, 
#    15: {"Магічні методи": 0}, 
# }


def read_topic_json():
    with open("dict_topic.json") as fd:
        result = json.load(fd)
    return result


dict_of_topic = read_topic_json()


def helps():
    result = """
            Список команд:
* Добавити картки для вивчення: <add> <номер теми> .    Наприклад: add 2
* Видалити картки для вивчення: <remove> <номер теми>.  Наприклад: remove 10
* Перейти до вивчення карток < ok >
    
            Номера тем:
===============================
"""
    for num_topic, topic in dict_of_topic.items():
        num_topic = str(num_topic).rjust(2, " ")

        topic = tuple(topic)[0]
        line = f"{num_topic}:  {topic}\n"
        result += line
    result += "==============================="
    return result



def parser():
    print(helps())
    while True:
        answer = input("Введіть команду:\n")
        try:
            command, num = answer.strip().lower().split()
        except:
            print("Повторіть команду за шаблоном:")
            print(helps())
        else:
            if num not in dict_of_topic:
                print(f"\nТеми №{num} не існує\n")
            else:
                for num_topic, topic in dict_of_topic.items():
                    if int(num_topic) == int(num):
                        if command == "add":
                            topic = tuple(topic)[0]
                            dict_of_topic[num][topic] = 1
                            print(f'Картки для вивчення теми "{topic}" добавлено.\n')
                            save_dict_topic()
                            break
                        elif command == "remove":
                            topic = tuple(topic)[0]
                            dict_of_topic[num][topic] = 0
                            print(f'Картки теми "{topic}" видалено зі списку вивчення.\n')
                            save_dict_topic()
                            break
                        else:
                            print("\nПовторіть команду за шаблоном:\n")
                            print(helps())
                    


def save_dict_topic():
    with open(r"dict_topic.json", "w", encoding= "utf-8") as fd:
        json.dump(dict_of_topic, fd, indent=4)



if __name__ == "__main__":
    print(parser())
    # save_dict_topic()

    

