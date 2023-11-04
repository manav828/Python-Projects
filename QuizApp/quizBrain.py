


class Brain:

    def __init__(self,que,ans):
        self.que = que
        self.ans = ans
        self.que_num = 0
        self.score = 0
        que_list = []

    def has_que(self):
        if self.que_num <len(self.que):
           que = self.question()
           return que
        else:
            return 0

    def question(self):
        question = self.que[self.que_num]
        return question

    def check_ans(self,ans):
        answer = self.ans[self.que_num]
        if answer == ans:
            self.score +=1
            if self.que_num-1<len(self.que):
                self.que_num += 1


            return 1
        else:
            if self.que_num - 1 < len(self.que):
                self.que_num += 1
                return 0

    def see_score(self):
        return self.score
