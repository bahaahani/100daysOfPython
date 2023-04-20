class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        correct_ans = self.question_list[self.question_number].answer
        self.check_ans(user_ans, correct_ans)
        self.question_number +=1

    def still_has_questions(self):
        return   self.question_number < len(self.question_list)

    def check_ans(self, user_ans,correct_ans):
        if user_ans == correct_ans:
            print("\nYou got that right\n")
            self.score += 1
        else:
            print(f"\nthats wrong! {correct_ans} is correct answer\n")
        print(f"Current Score is {self.score}/{self.question_number}")
        

