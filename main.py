


class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        # Додайте поле birthday для дня народження в клас Record.
        # Це поле має бути класу Birthday. Це поле не обов'язкове, але може бути тільки одне.
        self.birthday = None

# Додайте функціонал роботи з Birthday у клас Record, а саме функцію add_birthday, яка додає день народження до контакту.
    def add_birthday(self):
    
        pass

