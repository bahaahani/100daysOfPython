class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        correct_ans = self.current_question.answer
        self.check_ans(user_ans, correct_ans)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_ans(self, user_ans,correct_ans):
        return user_ans == correct_ans

