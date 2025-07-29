class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size  # Простой хеш-функция

    def insert(self, key, value):
        index = self._hash(key)  # Используем _hash
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Обновление существующего ключа
                return
        self.table[index].append([key, value])  # Добавление нового ключа

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:  # Проверка по ключу
                return pair[1]  # Возвращаем значение по ключу
        return None  # Если ключ не найден

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)  # Удаление элемента
                return True
        return False  # Если ключ не найден

# Пример использования
hash_table = HashTable(10)
hash_table.insert("apple", 2)
hash_table.insert("banana", 3)

print(hash_table.search("apple"))
print(hash_table.delete("banana"))
print(hash_table.search("banana"))