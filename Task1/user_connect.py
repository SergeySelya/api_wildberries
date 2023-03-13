def check_relation(net: tuple, first: str, second: str):

    peoples = dict()

    for friend in net:
        if friend[0] not in peoples:
            peoples[friend[0]] = set()
        if friend[1] not in peoples:
            peoples[friend[1]] = set()
        if friend[0] in peoples:
            peoples[friend[0]].add(friend[1])
        if friend[1] in peoples:
            peoples[friend[1]].add(friend[0])

    friends = {first: peoples[first], second: peoples[second]}

    for key, values in peoples.items():
        values.add(key)
        if not friends[first].isdisjoint(values):
            friends[first].update(values)
        if not friends[second].isdisjoint(values):
            friends[second].update(values)

    return True if not friends[first].isdisjoint(friends[second]) else False


if __name__ == "__main__":
    net = (
        ("Ваня", "Лёша"),
        ("Лёша", "Катя"),
        ("Ваня", "Катя"),
        ("Вова", "Катя"),
        ("Лёша", "Лена"),
        ("Оля", "Петя"),
        ("Стёпа", "Оля"),
        ("Оля", "Настя"),
        ("Настя", "Дима"),
        ("Дима", "Маша"),
    )
    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
