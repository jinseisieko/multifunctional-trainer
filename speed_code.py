import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class TypingTrainer(QMainWindow):
    def __init__(self, text):
        super().__init__()

        self.text = text
        self.input_text = ''
        self.errors = 0

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Тренажер слепой печати')
        self.setGeometry(200, 200, 400, 200)

        self.label_text = QLabel(self.text, self)
        self.label_text.setGeometry(50, 50, 300, 30)

        self.label_input = QLabel('Введите текст:', self)
        self.label_input.setGeometry(50, 90, 100, 30)

        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(160, 90, 150, 30)

        self.button_submit = QPushButton('Проверить', self)
        self.button_submit.setGeometry(160, 130, 80, 30)
        self.button_submit.clicked.connect(self.check_input)

        self.label_errors = QLabel('Количество ошибок: 0', self)
        self.label_errors.setGeometry(50, 170, 300, 30)

    def check_input(self):
        self.input_text = self.text_input.text()
        self.errors = sum(a != b for a, b in zip(self.text, self.input_text))
        self.label_errors.setText('Количество ошибок: {}'.format(self.errors))

        if self.text == self.input_text:
            self.text_input.setEnabled(False)
            self.button_submit.setEnabled(False)
            self.label_errors.setText('Тренировка завершена!')

        self.text_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    text = "The quick brown fox jumps over the lazy dog."
    trainer = TypingTrainer(text)
    trainer.show()
    sys.exit(app.exec_())
