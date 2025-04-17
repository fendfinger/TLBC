
from flask import Flask, render_template_string
from pytrends.request import TrendReq

app = Flask(__name__)

def get_daily_trends():
    pytrends = TrendReq(hl='ko', tz=540)
    df = pytrends.trending_searches(pn='south_korea')
    return df[0].tolist()[:10]

@app.route("/")
def home():
    trends = get_daily_trends()
    return render_template_string("""
        <h1>📈 오늘의 인기 검색어 (대한민국)</h1>
        <ul>
        {% for trend in trends %}
            <li>{{ trend }}</li>
        {% endfor %}
        </ul>
    """, trends=trends)

if __name__ == "__main__":
    app.run(debug=True)
