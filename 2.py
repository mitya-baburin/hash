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

    def resize(self):
        old_table = self.table  # Сохраняем старую таблицу
        self.size *= 2  # Увеличиваем размер таблицы
        self.table = [[] for _ in range(self.size)]  # Создаём новую таблицу

        for bucket in old_table:  # Перераспределение элементов
            for key, value in bucket:
                self.insert(key, value)  # Вставляем элементы в новую таблицу


# Пример использования
hash_table = HashTable(10)
hash_table.insert("apple", 2)
hash_table.insert("banana", 3)

print(hash_table.search("apple"))
print(hash_table.delete("banana"))
print(hash_table.search("banana"))

# Тестирование метода resize
for i in range(10):
    hash_table.insert(f"key{i}", i)

print("Размер таблицы после вставки 10 элементов:", hash_table.size)  # Вывод нового размера таблицы