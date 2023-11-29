from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3 as sql 
import base64
from pydantic import BaseModel

app = FastAPI()
connections = sql.connect('database.db')

origins = [
    "http://localhost:5173",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Image(BaseModel):
    img: str

    def getImg(self):
        return self.img

def writeImg(file,img):
    with open(file, 'wb') as f:
        f.write(img)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/recognition")
def recognition(item: Image):
    img_bytes = base64.b64decode(item.getImg().encode('utf-8'))
    writeImg('img/img.jpg', img_bytes)
    return {"img": item.getImg()}