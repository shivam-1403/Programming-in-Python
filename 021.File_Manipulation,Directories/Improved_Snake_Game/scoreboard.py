from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class ScoreBoard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"Programming-in-Python\021.File_Manipulation,Directories\Improved_Snake_Game\data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self) :
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(r"Programming-in-Python\021.File_Manipulation,Directories\Improved_Snake_Game\data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
    
    # def game_over(self) :
    #     self.goto(0, 0)
    #     self.write("Game Over.", align = ALIGNMENT, font = FONT)

    def increase_score(self) :
        self.score += 1
        self.update_scoreboard()