brothers_names = [
    "Aapo",
    "Eero",
    "Juhani",
    "Lauri",
    "Simeoni",
    "Timo",
    "Tuomas",
]


def seven_brothers():
    brothers_names.sort()
    for name in brothers_names:
        print(name)


if __name__ == "__main__":
    seven_brothers()
