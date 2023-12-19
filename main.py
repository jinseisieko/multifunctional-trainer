from EstimateQuestionAnswer import EstimateQuestionAnswer
from QuestionAnswer import QuestionAnswer
from TranslationEnglishSimulator import TranslationEnglishSimulator

qa = TranslationEnglishSimulator()
qa.add_file(r"tests\english translation\vocabulary dictation.txt")
while input() == "":
    qa.start_test(3)
    print(qa)
