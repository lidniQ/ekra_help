from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from bs4 import BeautifulSoup
import os
import uuid
import time
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно изменить на разрешенные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

upload_content ="/work/projects/ekra_help/help/src/data/json/articles.json"

class Content(BaseModel):
    content: str

@app.post("/save/content/")
async def receive_content(content: Content):
    received_content = content.content
    
    # Проверяем, не пуст ли заголовок
    if not has_title(received_content):
        raise HTTPException(status_code=400, detail="Заголовок не может быть пустым")
    
    json_load(parsing(received_content))
    print(received_content)
    return {"message": received_content}

def has_title(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return bool(soup.find('h1'))

def parsing(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    expanded = False  
    list_h2 = []
    
    films = soup.find('h1').text
    h2s = soup.find_all('h2')
    for h2 in h2s:
        h2string = h2.text
        list_h2.append(h2string)
        
    # Удаляем пустой список items
    if not list_h2:
        new_article = {
            "title": films,
            "expanded": False,
            "html": str(soup)
        }
    else:
        new_article = {
            "title": films,
            "expanded": False,
            "html": str(soup),
            "items": list_h2
        }
        
    return new_article

def json_load(new_article):
    with open(upload_content, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
    for article in data.get("articles", []):
        if article.get("title") == new_article["title"]:
            article["expanded"] = new_article["expanded"]
            article["html"] = new_article["html"]
            article["items"] = new_article["items"]
            break
    else:
        data.setdefault("articles", []).append(new_article)

    with open(upload_content, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4,ensure_ascii=False)


# Указываем путь к папке для сохранения файлов
UPLOAD_FOLDER = "/work/projects/ekra_help/help/src/media"


@app.post("/upload_image/")
async def upload_image(image: UploadFile = File(...)):
    try:
        # Генерация уникального имени файла
        unique_filename = time.strftime("%Y%m%d_%H_%M_%S_") + uuid.uuid4().hex[:6]
        # Сохранение изображения по уникальному имени
        with open(f"/work/projects/ekra_help/help/src/media/{unique_filename}.png", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        print("Image uploaded successfully")
        return JSONResponse(status_code=201, content={"message": "Image uploaded successfully", "imageUrl": f"{UPLOAD_FOLDER}/{unique_filename}.png"})
    except Exception as e:
        print(f"Failed to upload image: {str(e)}")
        return JSONResponse(status_code=500, content={"message": f"Failed to upload image: {str(e)}"})
