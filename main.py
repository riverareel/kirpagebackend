from fastapi import FastAPI, Request, Header
import json
from time import sleep
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
from telebot import TeleBot
from fastapi.responses import RedirectResponse
bot1 = TeleBot("5463120320:AAEDXKo6B3yzK2kZqDtX-j6M9Km4Sd54kgA")
bot2 = TeleBot("5314173046:AAHm7n4vMDMhWK4x6NHYmsWOYskQrQsLcdk")
bot3 = TeleBot("5426530816:AAHNb9br4nHhyqgDlUe4p3FvOXu6n8QWNiQ")
bot4 = TeleBot("5475071987:AAFSrIi56f29kcUaB0z6R_OhNX0xEkwJOVI")
bot5 = TeleBot("5522125769:AAGVhGmhFkeWbNlJawIDm576b1-yALcpRmE")
bot6 = TeleBot("5571413724:AAHpbw84ptHTnGSGsXJMLAVDT7npctXB3BQ")
bot7 = TeleBot("5533057599:AAH5K824MTTiRdhscV-Wb8Dk-MJYW1io058")

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
    ipAddress: str

@app.get("/")
async def root():
    return {"message": "Server is running properly. Made by KIR SMAN 2 Jakarta."}

@app.get("/ping")
async def serverResponse():
    return {"message": "Pong!"}

@app.post("/register")
async def register(request: Request, userData: userData, user_agent: str | None = Header(default=None)):
    consDict = {"name" : userData.name, "userClass" : userData.userClass, "phoneNumber" : userData.phoneNumber, "ts" : str(int(time.time())), "device_info" : {"user_agent" : user_agent, "x-ip" : str(userData.ipAddress)}, "message": "User registered successfully."}
    if len(userData.name) < 3:
        return {"message": "Oops! Pastikan kolom NAMA yang kamu isi sudah sesuai.",
                "status_code": 400}
    if len(userData.userClass) < 1:
        return {"message": "Oops! Pastikan kolom KELAS yang kamu isi sudah sesuai.",
                "status_code": 400}
    if len(userData.phoneNumber) < 9:
        return {"message": "Oops! Pastikan kolom Nomor Telepon yang kamu isi sudah sesuai.",
                "status_code": 400}
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
    while True:
        try:
            sender = random.choice([bot1, bot2, bot3, bot4, bot5, bot6, bot7])
            sender.send_message(messagecid, constructString, parse_mode="HTML", disable_web_page_preview=True)
            break
        except:
            sleep(3)
            continue
    return {"message": "OK",
            "status_code": 200}
