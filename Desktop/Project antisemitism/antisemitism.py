import sqlite3

conn = sqlite3.connect('antisemitism.db')
cursor = conn.cursor()

def get_articles():
    query = "SELECT * FROM articles;"
    cursor.execute(query)
    articles = cursor.fetchall()
    return articles

def get_testimonies():
    query = "SELECT * FROM testimonies;"
    cursor.execute(query)
    testimonies = cursor.fetchall()
    return testimonies




if __name__ == "__main__":
    articles = get_articles()
    print("Articles:")
    for article in articles:
        print(article)

    testimonies = get_testimonies()
    print("\nTémoignages:")
    for testimony in testimonies:
        print(testimony)

conn.close()


class Question:
    def __init__(self, text, options, correct_option, explanation):
        self.text = text
        self.options = options
        self.correct_option = correct_option
        self.explanation = explanation

    def is_correct(self, answer):
        return answer == self.correct_option


def run_quiz(questions):
    score = 0

    print("Bienvenue au Quiz de Sensibilisation contre l'antisémitisme!\nRépondez en entrant le numéro de l'option correcte.\n")

    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question.text}")
        for j, option in enumerate(question.options, 1):
            print(f"{j}. {option}")

        user_answer = int(input("Votre réponse : "))

        if question.is_correct(user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Faux. La réponse correcte était l'option {question.correct_option}.")
            print(f"Explication : {question.explanation}\n")

    print(f"Score final : {score}/{len(questions)}")


question1 = Question("Qu'est-ce que l'antisémitisme?", ["Hostilité envers les sémites", "Amour envers les sémites", "Indifférence envers les sémites", "Peur des sémites"], 1, "L'antisémitisme est une forme de discrimination dirigée contre les personnes d'origine sémitique, principalement les Juifs.")
question2 = Question("Quel événement historique est souvent associé à l'antisémitisme?", ["La Renaissance", "La Révolution industrielle", "L'Holocauste", "La Guerre froide"], 3, "L'Holocauste pendant la Seconde Guerre mondiale a été un exemple extrême d'antisémitisme, où des millions de Juifs ont été persécutés et tués.")
question3 = Question("Comment pouvons-nous lutter contre l'antisémitisme?", ["Ignorer le problème", "Promouvoir l'éducation et la tolérance", "Encourager la discrimination", "Éviter la diversité culturelle"], 2, "La promotion de l'éducation, de la tolérance et de la compréhension contribue à lutter contre l'antisémitisme et la discrimination.")


quiz_questions = [question1, question2, question3]

run_quiz(quiz_questions)



