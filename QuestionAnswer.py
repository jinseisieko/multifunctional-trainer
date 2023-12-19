class QuestionAnswer:
    def __init__(self):
        super().__init__()
        self.question_answer = []

    def add(self, question, answer):
        for i, question_answer_ in enumerate(self.question_answer):
            question_ = question_answer_[0]
            answer_ = question_answer_[1]
            if question_ == question and answer_ == answer:
                break
        self.question_answer.append((question, answer))

    def add_one_line(self, string, sep_=";"):
        question, answer = string.split(sep_)
        question = question.strip()
        answer = answer.strip()
        self.add(question, answer)

    def add_file(self, file_name, sep_=";"):
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                self.add_one_line(line, sep_)

    def del_(self, question, answer):
        for i, question_answer_ in enumerate(self.question_answer):
            question_ = question_answer_[0]
            answer_ = question_answer_[1]
            if question_ == question and answer_ == answer:
                self.question_answer.pop(i)
                break

    def save_file_txt(self, file_name, sep_=";"):
        with open(file_name, "w", encoding="utf-8") as file:
            for question, answer in self.question_answer:
                file.write(f"{question}{sep_}{answer}\n")

    def __str__(self):
        string = ""
        for question, answer in self.question_answer:
            string += f"\n({question}, {answer})"
        return f"{len(self.question_answer)}: \n" + string
