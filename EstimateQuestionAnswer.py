from QuestionAnswer import QuestionAnswer


class EstimateQuestionAnswer(QuestionAnswer):
    def __init__(self):
        super().__init__()
        self.grades = {}

    def estimate(self, question, good):
        if question in self.grades:
            self.grades[question] += 1 if good else -1
        else:
            self.grades[question] = 1 if good else -1

    def __str__(self):
        string = ""
        for question, answer in self.question_answer:
            string += f"\n({question}, {answer}, "
            if question in self.grades:
                string += f"{self.grades[question]})"
            else:
                string += "0)"
        return f"{len(self.question_answer)}:" + string
