from EstimateQuestionAnswer import EstimateQuestionAnswer
from QuestionAnswer import QuestionAnswer
from TranslationEnglishSimulator import TranslationEnglishSimulator

qa = TranslationEnglishSimulator()
qa.add_file(r"tests\english translation\vocabulary dictation.txt")
qa.start_test()
qa.start_test()
print(qa)
