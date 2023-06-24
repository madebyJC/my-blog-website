import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)

current_year = datetime.datetime.now().year


@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()

    return render_template('index.html', posts=all_posts, year=current_year)


@app.route('/post/<int:num>')
def get_post(num):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()

    return render_template('post.html', posts=all_posts, num=num, year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
