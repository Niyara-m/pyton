import sqlite3
connection = sqlite3.connect("mydatabase.db")
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, grade TEXT);")
connection.commit()

# sql.execute('INSERT INTO students (name, age, grade) VALUES("Nika", 20, "2B");')
# sql.execute('INSERT INTO students (name, age, grade) VALUES("Roma", 22, "3B");')
# sql.execute('INSERT INTO students (name, age, grade) VALUES("Rima", 25, "4B");')

connection.commit()

#Функция возвращает информацию о студенте
def get_student_by_name(name):
    student_info = sql.execute('SELECT * FROM students WHERE name=?;', (name,)).fetchone()
    print(f'id: {student_info[0]}, Имя студента: {student_info[1]}, Возраст: {student_info[2]}, Оценка: {student_info[3]}')

get_student_by_name('Roma');

#Функция обновляет оценку студента
def update_student_grade(name, grade):
    sql.execute(f'UPDATE students SET grade={grade}  WHERE name=?;', (name,))
    connection.commit()
    info = sql.execute('SELECT * FROM students WHERE name=?;', (name,)).fetchone()
    print(f'Обновленные данные для студента {info}')

update_student_grade('Roma','8900');

print(f'Все данные таблицы: {sql.execute("SELECT * from students").fetchall()}')

#Функция удаляет данные студента
def delete_student(name):
    sql.execute('DELETE FROM students WHERE name=?;', (name,))
    connection.commit()
    print(f'Оставшиеся данные таблицы: {sql.execute("SELECT * from students").fetchall()}')
delete_student('Rima');