import csv

class Question:
    def __init__(self, choice_a, choice_b, score_a, score_b):
        # a question consist of 2 choices, and what type the questions contribute to
        self.choice_a = choice_a  # "I've been romantic and imaginative."
        self.choice_b = choice_b  # "I've been pragmatic and down to earth."
        self.score_a = score_a  # "E"
        self.score_b = score_b  # "B"

def read_questions_from_csv(filename):
    with open(filename, 'r') as questions_csv:
        reader = csv.reader(questions_csv, delimiter=',')
        questions = []
        for row in reader:
            if row:
                q = Question(row[0],row[1], row[2], row[3])
                questions.append(q)
        return questions

questions = read_questions_from_csv(filename = 'questions.csv')

# Now 'questions' contains a list of Question objects
# You can iterate over the list and access the attributes of each Question object
for question in questions:
    print(question.choice_a, question.choice_b, question.score_a, question.score_b)









     