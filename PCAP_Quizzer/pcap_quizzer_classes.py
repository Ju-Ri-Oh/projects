class Quiz:
    def __init__(self, quiz_id):
        self.quiz_id = quiz_id


class Databank:
    def __init__(self, databank_id):
        self.databank_id = databank_id


class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name


class Subcategory:
    def __init__(self, subcategory_id, subcategory_name):
        self.subcategory_id = subcategory_id
        self.subcategory_name = subcategory_name
        # TO DO: Foreign key to Category


class Question:
    def __init__(self, question_text, explanation):
        self.question_text = question_text
        self.explanation = explanation
        # TO DO: Foreign key to Category, Subcategory
        


class Option:
    def __init__(self, option_text, correct_answer ):
        self.option_text = option_text
        self.correct_answer = correct_answer
        # TO DO: Foreign key to Question