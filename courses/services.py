from config import settings
from courses.models import Test, Question, Answer


def user_testing(user, test_id):
    # Получаем тест по ID

    test = Test.objects.get(id=test_id)

    # Получаем все вопросы для данного теста
    questions = Question.objects.filter(test=test)

    # Создаем словарь для хранения ответов пользователя
    user_answers = {}

    # Проходимся по каждому вопросу и запрашиваем ответ пользователя
    for question in questions:
        print(question.question_text)
        user_answer = input("Введите ваш ответ: ")
        user_answers[question.id] = user_answer

    # Проверяем ответы пользователя и выводим результат
    score = 0
    for question in questions:
        user_answer = user_answers[question.id]
        correct_answers = Answer.objects.filter(question=question, is_correct=True)
        if user_answer in [answer.answer_text for answer in correct_answers]:
            score += 1

    print(f"Вы набрали {score} из {len(questions)} баллов")

# Пример использования функции
user_testing(user=settings.AUTH_USER_MODEL, test_id=1)
