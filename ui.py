from tkinter import *
from quiz_brain import QuizBrain

BACKGROUND_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzopedia")
        self.window.config(padx=20, pady=20, background=BACKGROUND_COLOR)

        # Score Board
        self.scoreboard = Label(master=self.window, text="Score: 0", bg=BACKGROUND_COLOR, fg="white")
        self.scoreboard.grid(row=0, column=1)

        # Canvas for question
        self.canvas = Canvas(master=self.window, width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Question text",
                                                     fill=BACKGROUND_COLOR,
                                                     font=QUESTION_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(master=self.window, image=true_image, highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=3, column=0)

        # False Button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(master=self.window, image=false_image, highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text="Quiz finished.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(u_answer="True")
        self.feedback_card(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer(u_answer="False")
        self.feedback_card(is_right)

    def feedback_card(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.scoreboard.configure(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)
