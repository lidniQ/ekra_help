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
import base64
from fastapi.staticfiles import StaticFiles

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
    title: str

@app.post("/save/content/")
async def receive_content(content: Content):
    received_content = content.content
    received_title = content.title
    # Проверяем, не пуст ли заголовок
    if not has_title(received_content):
        raise HTTPException(status_code=400, detail="Заголовок не может быть пустым")
    
    json_load(parsing(received_content),received_title)
    return {"message": received_title}

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



def json_load(new_article, check_value):
    with open(upload_content, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
    for article in data.get("articles", []):
        if article.get("title") == new_article["title"] or article.get("title") == check_value:
            article["title"] = new_article["title"]  # Обновление заголовка
            article["expanded"] = new_article["expanded"]
            article["html"] = new_article["html"]
            article["items"] = new_article["items"]
            break
    else:
        data.setdefault("articles", []).append(new_article)

    with open(upload_content, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)





# Указываем путь к папке для сохранения файлов
UPLOAD_FOLDER = "/work/projects/ekra_help/help/src/media/"

app.mount("/img", StaticFiles(directory=UPLOAD_FOLDER+'/Image'), name="static")
app.mount("/video", StaticFiles(directory=UPLOAD_FOLDER+'/Video'), name="static")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload_image/")
async def upload_image(image: UploadFile = File(...)):
    try:
        # Генерация уникального имени файла
        unique_filename = time.strftime("%Y%m%d_%H_%M_%S_") + uuid.uuid4().hex[:6]
        # Сохранение изображения по уникальному имени
        with open(f"{UPLOAD_FOLDER}/Image/{unique_filename}.png", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        print("Изображение успешно загружено")
        file_url = f"http://10.27.1.6:8000/img/{unique_filename}.png"  # Изменяем URL-адрес для доступа к статическим файлам
        return {"file_url": file_url}    
    except Exception as e:
        print(f"Не удалось загрузить изображение: {str(e)}")
        return JSONResponse(status_code=500, content={"message": f"Не удалось загрузить изображение: {str(e)}"})


@app.post("/upload_video/")
async def upload_image(video: UploadFile = File(...)):
    try:
        # Генерация уникального имени файла
        unique_filename = time.strftime("%Y%m%d_%H_%M_%S_") + uuid.uuid4().hex[:6]
        # Сохранение изображения по уникальному имени
        with open(f"{UPLOAD_FOLDER}/Video/{unique_filename}.mp4", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)
        print("Видео успешно загружено")
        file_url = f"http://10.27.1.6:8000/video/{unique_filename}.mp4"  # Изменяем URL-адрес для доступа к статическим файлам
        return {"file_url": file_url}    
    except Exception as e:
        print(f"Не удалось загрузить видео: {str(e)}")
        return JSONResponse(status_code=500, content={"message": f"Не удалось загрузить видео: {str(e)}"})
