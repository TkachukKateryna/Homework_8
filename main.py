from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if len(users) == 0:
        return {}
    now = date.today()
    result = {}
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    for user in users:
        birthday = user.get('birthday').replace(year=now.year)
        if birthday < now:
            birthday = user.get('birthday').replace(year=now.year+1)
            
        if now <= birthday <= now + timedelta(days=7):
            if birthday.weekday() <= 4:
                if weekdays[birthday.weekday()] in result:
                    result[weekdays[birthday.weekday()]].append(user.get("name"))
                elif weekdays[birthday.weekday()] not in result:
                    result[weekdays[birthday.weekday()]] = [(user.get("name"))]
            elif birthday.weekday() == 5 or birthday.weekday() == 6:
                if weekdays[0] in result:
                    result[weekdays[0]].append(user.get("name"))
                elif weekdays[0] not in result:
                    result[weekdays[0]] = [(user.get("name"))]   
        else:
            pass
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")