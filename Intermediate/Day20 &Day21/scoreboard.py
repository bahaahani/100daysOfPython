import turtle
import random
class Scoreboard(turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        