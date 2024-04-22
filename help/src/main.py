from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Content(BaseModel):
    content: str

@app.post("/receive_content/")
async def receive_content(content: Content):
    # Здесь вы можете обработать полученный контент
    received_content = content.content
    # Делайте что-то с полученным контентом, например, выводите его
    print(received_content)
    # Верните какой-то ответ, если это необходимо
    return {"message": "Content received successfully"}
