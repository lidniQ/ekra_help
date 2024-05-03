from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class Content(BaseModel):
    content: str

@app.post("/save/content/")
async def receive_content(content: Content):
    received_content = content.content
    print(received_content)
    return {"message": received_content}
