from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/guess/<name>")
def hello(name):
    new_name = name.title()
    parameters = {
        "name" : name,
    }
    age_guess = requests.get("https://api.agify.io?name=michael", params=parameters)
    gender_guess = requests.get("https://api.genderize.io?", params=parameters)
    age_data = age_guess.json()
    gender_data = gender_guess.json()
    age = age_data["age"]
    gender = gender_data["gender"]
    return render_template('index.html', name=new_name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)