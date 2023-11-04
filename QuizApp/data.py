import requests



class data:
    def __init__(self):
        response = requests.get(url='https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')
        data = response.json()

        response.raise_for_status()
        self.que_list =[]
        self.ans_list =[]

        for que in data['results']:

            self.que_list.append(que['question'])
            self.ans_list.append(que['correct_answer'])

