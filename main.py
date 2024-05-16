from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ConPDf import call_api_IA

app = FastAPI()


class Message(BaseModel):
    text: str


@app.post("/chat/")
async def chat(message: Message):
    # Invoca la IA con el mensaje del usuario
    respuesta = call_api_IA(message.text)
    return {"status": "200 OK", "respuesta": respuesta}


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "https://pruebaapi.netlify.app",
    "https://hechizera10.github.io/ChatBot-Front/",
    "https://hechizera10.github.io",
    "https://utn-frsr-tup.github.io/ChatBot-Front/",
    "https://utn-frsr-tup.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"]  # Exponer el encabezado Allow-Origin
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

