from flask import Flask
import random

number = random.randint(0,9)
print(number)
app = Flask(__name__)

@app.route("/")
def game_title():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjl3dGpxeWtsdm0yOHI2bWxvemxpcW5tb3piejVxb243ZW92OXhidSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:num>")
def play(num):
    if num == number:
        return "<h2 style='color : green'>You Found Me!</h2>" \
        "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm80MXVua2xocHVuY3VlNGlzMHEydHo2eHltdG9xeXN0M2FoYzVtaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4T7e4DmcrP9du/giphy.gif'>"
    elif num > number:
        return "<h2 style='color : purple'>It's High, try again!</h2>" \
        "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNW12cXIzaHFqdnhyZ21xazdxcDV4b2UzNHFzeHNtZXV4b3A5cmxhayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h2 style='color : red'>It's Low, try again!</h2>" \
        "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNThjb3Z6ZHFmdXJ6dmxkamVodHEzZnZqZTcyM3l6bjdkbTFlazRqbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jD4DwBtqPXRXa/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)