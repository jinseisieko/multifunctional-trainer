import random

from EstimateQuestionAnswer import EstimateQuestionAnswer


class TranslationEnglishSimulator(EstimateQuestionAnswer):
    def add(self, question, answer):
        super().add(question, answer)
        super().add(answer, question)

    @staticmethod
    def get_user_answer(question):
        return input(f"{question}: ")

    def start_test(self, count=1):
        question_answer = self.question_answer.copy() * count
        random.shuffle(question_answer)
        for question, answer in question_answer:
            user_answer = self.get_user_answer(question)
            if user_answer.lower() == answer.lower():
                print("Правильный ответ!\n----------------\n")
                self.estimate(question, True)
            else:
                print("Неправильный ответ!")
                print(f"Правильный ответ: {answer}\n----------------\n")
                self.estimate(question, False)
