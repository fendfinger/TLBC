from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()

app = Flask(__name__)

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

@app.route("/")
def index():
    return "네이버 트렌드 API 작동 중!"

@app.route("/trend")
def get_trend():
    url = "https://openapi.naver.com/v1/datalab/search"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
        "Content-Type": "application/json"
    }

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=7)

    data = {
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d"),
        "timeUnit": "date",
        "keywordGroups": [
            {
                "groupName": "프로그래밍",
                "keywords": ["프로그래밍", "코딩", "파이썬"]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return f"Error: {response.status_code} - {response.text}"
