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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render에서 자동으로 할당해줌
    app.run(host='0.0.0.0', port=port)        # 외부에서 접속 가능하게 지정
