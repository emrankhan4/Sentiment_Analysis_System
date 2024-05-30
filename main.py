from userlib import *
from fastapi import FastAPI
app = FastAPI()



@app.get('/')
def get_model():
    return {'Welcome. Please visit http://127.0.0.1:8000/sentiment for sentiment analysis'}

@app.post('/sentiment')
def get_sentiment(txt):
    print(txt)
    print(type(predict(txt)))
    return f"{predict(txt)}"



