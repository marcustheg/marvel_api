import marvel

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return 'welcome to marcus` random marvel hero generator!'

@app.route('/heroes/random/<int:series>')
def heroes_page(series):
    character_resp = marvel.get_characters_by_series(series)
    name = marvel.random_character_name(character_resp)
    return 'welcome to the heroes page.' + name

