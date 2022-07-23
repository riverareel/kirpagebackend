from fastapi import FastAPI, Request, Header
import json
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from telebot import TeleBot
bot = TeleBot("5463120320:AAEDXKo6B3yzK2kZqDtX-j6M9Km4Sd54kgA")
import time

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class userData(BaseModel):
    name: str
    userClass: str
    phoneNumber: str

@app.get("/")
async def root():
    return {"message": "Server is running properly. Made by KIR SMAN 2 Jakarta."}

@app.get("/ping")
async def serverResponse():
    return {"message": "Pong!"}

@app.post("/register")
async def register(request: Request, userData: userData, user_agent: str | None = Header(default=None)):
    consDict = {"name" : userData.name, "userClass" : userData.userClass, "phoneNumber" : userData.phoneNumber, "ts" : str(int(time.time())), "device_info" : {"user_agent" : user_agent, "x-ip" : str(request.headers.get("HTTP_CF_CONNECTING_IP"))}, "message": "User registered successfully."}
    if len(userData.name) < 3:
        return {"message": "Oops! Pastikan kolom NAMA yang kamu isi sudah sesuai.",
                "status": 400}
    if len(userData.userClass) < 1:
        return {"message": "Oops! Pastikan kolom KELAS yang kamu isi sudah sesuai.",
                "status": 400}
    if len(userData.phoneNumber) < 9:
        return {"message": "Oops! Pastikan kolom Nomor Telepon yang kamu isi sudah sesuai.",
                "status": 400}
    with open("data.json", "a") as outfile:
        outfile.write(str(consDict) + ",\n")
    outfile.close()
    constructString = f"""
<pre>
ADIK BAROE! ✊

Nama   : </pre><pre>{userData.name}</pre><pre>
Kelas  : {userData.userClass}
</pre>
<pre>No. Telp  : </pre><pre>{userData.phoneNumber}</pre><pre>
Link WhatsApp  :</pre> https://wa.me/62{userData.phoneNumber}"""
    messagecid = -1001574503712
    bot.send_message(messagecid, constructString, parse_mode="HTML", disable_web_page_preview=True)
    return {"message": "OK",
            "status": 200}
