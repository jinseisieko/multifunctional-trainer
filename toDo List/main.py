import random
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import QSize

# Создание базы данных или подключение к существующей
conn = sqlite3.connect('todolist.db')
cursor = conn.cursor()
# Создание таблицы для задач, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL
)
''')
conn.commit()


class TodoList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ToDo List')
        self.setFixedSize(400, 600)  # Установка фиксированного размера окна

        self.layout = QVBoxLayout()

        # Создание списка дел
        self.todo_list = QListWidget()
        self.layout.addWidget(self.todo_list)

        # Создание строки ввода и кнопки добавления
        self.input_box = QLineEdit()
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.add_task)

        # Кнопка для добавления "Foxford"
        self.add_foxford_button = QPushButton('Add Foxford')
        self.add_foxford_button.clicked.connect(self.add_foxford)

        # Создание кнопки удаления
        self.remove_button = QPushButton('Remove Selected')
        self.remove_button.clicked.connect(self.remove_task)

        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.input_box)
        self.input_layout.addWidget(self.add_button)
        self.input_layout.addWidget(self.add_foxford_button)

        self.remove_layout = QHBoxLayout()
        self.remove_layout.addStretch()
        self.remove_layout.addWidget(self.remove_button)

        self.layout.addLayout(self.input_layout)
        self.layout.addLayout(self.remove_layout)

        self.setLayout(self.layout)

        self.load_tasks()

    def add_task(self):
        task = self.input_box.text()
        if task:
            # Добавление задачи в базу данных
            cursor.execute('INSERT INTO tasks (description) VALUES (?)', (task,))
            conn.commit()
            # Добавление задачи в список интерфейса
            self.todo_list.addItem(task)
            self.input_box.clear()

    def add_foxford(self):
        names = ["Курс подготовки к ЕГЭ по информатике, 10 класс",
                 "Подготовка к вузовским олимпиадам по информатике для 10–11 классов",
                 "Авторский курс подготовки к ЕГЭ по физике от Михаила Пенкина, 10 класс",
                 "Подготовка к вузовским олимпиадам по физике «Физтех», «Росатом», «Ломоносов» для 10–11 классов",
                 "Курс подготовки к ЕГЭ по русскому языку, 10 класс",
                 "Авторский курс подготовки к ЕГЭ-2024 по профильной математике от Бориса Трушина с 0 до 70 баллов",
                 "Подготовка к олимпиадам «Физтех», «Ломоносов», «ОММО», «ПВГ» по математике для 10–11 классов",
                 "PRO Grammar boost: Грамматика английского языка продвинутого уровня",
                 "Курс по английскому языку Intermediate для 8-10 классов"]
        task = random.choice(names)
        cursor.execute('INSERT INTO tasks (description) VALUES (?)', (task,))
        conn.commit()
        self.todo_list.addItem(task)

    def remove_task(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            # Удаление задачи из базы данных
            cursor.execute('DELETE FROM tasks WHERE description = ?', (selected_item.text(),))
            conn.commit()
            # Удаление задачи из списка интерфейса
            self.todo_list.takeItem(self.todo_list.row(selected_item))

    def load_tasks(self):
        # Загрузка задач из базы данных
        cursor.execute('SELECT description FROM tasks')
        tasks = cursor.fetchall()
        for task in tasks:
            self.todo_list.addItem(task[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = TodoList()
    todo_app.show()
    sys.exit(app.exec_())

# Закрытие подключения к базе данных при выходе из приложения
cursor.close()
conn.close()
