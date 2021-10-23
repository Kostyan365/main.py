import sqlite3

try:
    print('ffgf')
    # Устанавливаем соединение с локальной базой данных
    conn = sqlite3.connect('..//base_date/vegetables.db')
    cursor = conn.cursor()

    # Если не существует таблиц, их нужно создать (первый запуск)
    vegetable = """
      create table if not exists
        vegetable (
            id INT,
            super_class TEXT,
            class TEXT,
            name TEXT,
            hybrid INT DEFAULT 0,
            type INT DEFAULT 0,
            boarding_time DATETIME
        );
    """
    cursor.execute(vegetable)
    conn.close()
except:
    print('Ошибка')
