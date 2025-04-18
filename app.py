from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 불러오기

app = Flask(__name__)

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

@app.route("/")
def index():
    return f"네이버 클라이언트 ID: {NAVER_CLIENT_ID}"
