from fastapi import FastAPI
import uvicorn
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello Anindya, Sameer and other Aditya Birla Capital colleagues and guests. This is a basic Azure website that I've built. This can call various Python functions easily. This is to give you confidence that to build a UI on Azure is simple and something that I can do easily. \n \n I have done this in my personal Azure account as doing this in our official setup requires port opening and other approvals which is time consuming. In my personal Azure account, I dont keep any resources running beyond the weekend to avoid incurring any bills. Hence I cant demonstrate anything fancy here to you. \n \n To give you further confidnence. Here's a simple output of a function that returns current time. Substituting this for an function that does any Generative AI related activities is a 2 minute effort. The time is: " + datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
