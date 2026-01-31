class Question:
    def __init__(self, q, a):
        self.question = q
        self.answer = a


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, q):
        self.questions.append(q)

    def start(self):
        for q in self.questions:
            ans = input(q.question + " ")
            if ans.lower() == q.answer.lower():
                self.score += 1

    def result(self):
        print("Natija:", self.score, "/", len(self.questions))


quiz = Quiz()
quiz.add_question(Question("Python kim tomonidan yaratilgan?", "Guido"))
quiz.add_question(Question("OOP nima?", "Object Oriented Programming"))

quiz.start()
quiz.result()
