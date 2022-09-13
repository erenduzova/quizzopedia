from data import question_data
from ui import QuizzInterface
from question_model import Question
from quiz_brain import QuizBrain


def create_question_bank(data):
    tmp_bank = []
    for question in data:
        q_text = question["question"]
        q_answer = question["correct_answer"]
        new_question = Question(q_text, q_answer)
        tmp_bank.append(new_question)
    return tmp_bank


question_bank = create_question_bank(data=question_data)

quiz = QuizBrain(question_bank)

quiz_ui = QuizzInterface(quiz)
