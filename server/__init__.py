import marvel
import logging

from flask import Flask, render_template, request
app = Flask(__name__)

gunicorn_logger = logging.getLogger('gunicorn.info')
app.logger.handlers = gunicorn_logger.handlers

@app.route('/')
def home_page():
    return render_template('hello.html')

# @app.route('/heroes/random/<int:series>')
# def heroes_page(series):
#     character_resp = marvel.get_characters_by_series(series)
#     name = marvel.random_character_name(character_resp)
#     return 'welcome to the heroes page.' + name
    
@app.route('/heroes/random', methods=['POST', 'GET'])
def random_heroes_page():
    # series =  request.form["series"]
    app.logger.info("something", request.form) 
    # return "okay" + series
    return "okay"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)