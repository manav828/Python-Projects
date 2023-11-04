import requests
from ui import quiz_ui
from data import data
from quizBrain import Brain
response = requests.get(url='https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')
response.raise_for_status()

# print(len(data['results']))


app_data = data()
que_list = app_data.que_list
ans_list = app_data.ans_list
quizBrain = Brain(que_list,ans_list)
app_ui = quiz_ui(quizBrain)

quiz_status = True

