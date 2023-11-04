from tkinter import *
from quizBrain import Brain
THEME_COLOR = '#3f679d'
class quiz_ui :

    def __init__(self,quiz_brain:Brain):
        self.quiz = quiz_brain
        self.score = quiz_brain.score
        self.window = Tk()

        self.window.title('Quizzler ')
        self.window.minsize(height=500,width=330)
        self.window.config(padx = 10,pady=10,background=THEME_COLOR)

        self.score_lable = Label(text=f'Score: {self.score}',fg='white',bg=THEME_COLOR)
        self.score_lable.grid(row=0,column=1)

        self.canvas = Canvas(width=300 , height=250,bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=200,
                                                     text="some twxt here",
                                                     fill=THEME_COLOR,
                                                     font=('Arial',20,'italic')
                                                     )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20,padx=10)

        self.true_btn = Button(text='TRUE', command=self.true)
        self.true_btn.grid(row=2,column=0)

        self.false_btn = Button(text='FALSE',command=self.false)
        self.false_btn.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()


    def true(self):
        ans = self.quiz.check_ans('True')
        print(ans)
        if ans == 1:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.score_lable.config(text=f'Score {self.quiz.score}')

        self.window.after(1000, self.get_question())

    def false(self):
        ans = self.quiz.check_ans('False')
        if ans == 1:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(self.canvas,bg='red')
        self.window.after(1000,self.get_question())




    def get_question(self):
        q_text = self.quiz.question()
        self.canvas.config(bg='white')
        if q_text == 0:
            self.canvas.itemconfig(self.question_text, text='game will ended')
        else:
            self.canvas.itemconfig(self.question_text,text = q_text)






