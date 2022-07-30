from models import Question


def create_mock_question():
    question = Question(
        question='test question',
        answer='test answer',
        difficulty=1,
        category='1')
    question.insert()
    return question.id
