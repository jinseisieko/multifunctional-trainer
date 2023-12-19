import random

from EstimateQuestionAnswer import EstimateQuestionAnswer


class TranslationEnglishSimulator(EstimateQuestionAnswer):
    def add(self, question, answer):
        super().add(question, answer)
        super().add(answer, question)

    @staticmethod
    def get_user_answer(question):
        return input(f"{question}: ")

    def start_test(self):
        question_answer = self.question_answer.copy()
        random.shuffle(question_answer)
        for question, answer in question_answer:
            user_answer = self.get_user_answer(question)
            if user_answer == answer:
                print("Правильный ответ!\n----------------")
                self.estimate(question, True)
            else:
                print("Неправильный ответ!")
                print(f"Правильный ответ: {answer}\n----------------")
                self.estimate(question, False)
