from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# For other task options, see https://huggingface.co/docs/transformers/en/main_classes/pipelines 
sentiment_pipeline = pipeline("sentiment-analysis")

app = FastAPI()

data = ["I love you", "I hate you"]
sentiment_pipeline(data)

class RequestModel(BaseModel):
    input_string: str

@app.post("/analyze")
def your_function(request: RequestModel):

    input_string = request.input_string

    sentiment = sentiment_pipeline(input_string)
    return {"result": 
            {"sentiment" : sentiment[0]["label"],
             "score" : sentiment[0]["score"]}
             }