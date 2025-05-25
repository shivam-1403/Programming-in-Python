from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    random_number = random.randint(1, 10)
    curr_year = datetime.now().year
    return render_template('index.html', num = random_number, year = curr_year)

if __name__ == "__main__":
    app.run(debug=True)