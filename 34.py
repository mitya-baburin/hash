#Функция для вычисления хеш-значения строки
def string_hash(s):
    return sum(ord(char) for char in s)    # Суммируем ASCII-коды символов

#Реализация хеш-таблицы
class Minisword:
    def __init__(self):
        self.data = {}    # Используем словарь Python для хранения данных

    def add(self, key):
        hash_value = string_hash(key)
        self.data[key] = hash_value    # Добавляем ключ и его хеш-значение

    def search(self, key):
        return self.data.get(key, None)    # Возврат хеш-значения по ключу или None, если не найден


dict = Minisword()
dict.add("apple")
dict.add("banana")

# Поиск значений по ключам
print(f"HASH for 'apple': {dict.search('apple')}")
print(f"HASH for 'banana': {dict.search('banana')}")
print(f"HASH for 'cat': {dict.search('orange')}")