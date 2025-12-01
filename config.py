# TEAM PURVI ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "26407378"
    API_HASH = "0f5b6504d2198c5f00af95975faa5ff2"
    #TOKEN = "8180856897:AAEGE9YvX9ggQ_4myGXqdj7fbbbMyO68K20"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://yadav99990hsjab:yadav99990hsjab@cluster0.78loh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://files.catbox.moe/ppvvg0.jpg"
    SUDOERS = filters.user(["5011400467"])
