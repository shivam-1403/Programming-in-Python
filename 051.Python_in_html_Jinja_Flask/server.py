from flask import Flask, render_template
import requests
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    random_number = random.randint(1, 10)
    curr_year = datetime.now().year
    return render_template('index.html', num = random_number, year = curr_year)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)