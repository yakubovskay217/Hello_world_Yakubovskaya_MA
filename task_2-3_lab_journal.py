create_journal_entry(researcher, date, experiment, conclusion):

    border = "--------------------------------------------------"

    content = f"""
| {border}
| ФИО исследователя : {researcher} |
| Дата : {date} |
| Эксперимент : {experiment} |
| {border}
| Вывод: |
| В ходе эксперимента выявлены {conclusion} |
| {border}
"""
    return content


def main():

    researcher = input("Введите ФИО исследователя: ")
    date = input("Введите дату (ДД.ММ.ГГГГ): ")
    experiment = input("Введите название эксперимента: ")
    conclusion = input("Введите вывод: ")


    entry = create_journal_entry(researcher, date, experiment, conclusion)


    with open("journal.txt", "w", encoding="utf-8") as file:
        file.write(entry)


if __name__ == "__main__":
    main()