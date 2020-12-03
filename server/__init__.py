import marvel
# import logging
import os
import falcon
import jinja2
import json


def load_template(name):
    path = os.path.join('server/templates', name)
    with open(os.path.abspath(path), 'r') as fp:
        return jinja2.Template(fp.read())

class StaticResource(object):
    def on_get(self, req, resp, filename):
        # do some sanity check on the filename
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/css'
        relpath = os.path.join('server/static', filename)
        abspath = os.path.abspath(relpath)
        with open(abspath, 'r') as f:
            resp.body = f.read()

class RandomCharacterApi(object):
    def on_get(self, req, resp):
        """Handles GET requests for marvel characters"""
        series = req.params["series"]
        character_resp = marvel.get_characters_by_series(series)
        name = marvel.random_character_name(character_resp)
        payload = {"name": name}
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps(payload)

class HelloResource(object):
    def on_get(self, req, resp):
        template = load_template('hello.html')
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = template.render()

class RandomCharacterResource(object):
    def on_get(self, req, resp):
        """Handles GET requests for marvel characters"""
        series = req.params["series"]
        character_resp = marvel.get_characters_by_series(series)
        name = marvel.random_character_name(character_resp)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = 'welcome to the heroes page.\n\n\t' + name

app = falcon.API()
app.add_route('/', HelloResource())
app.add_route('/static/{filename}', StaticResource())
app.add_route('/heroes/random/', RandomCharacterResource())
app.add_route('/api/heroes/random/', RandomCharacterApi())

# from flask import Flask, render_template, request
# app = Flask(__name__)

# gunicorn_logger = logging.getLogger('gunicorn.info')
# app.logger.handlers = gunicorn_logger.handlers

# @app.route('/')
# def home_page():
#     return render_template('hello.html')

# # @app.route('/heroes/random/<int:series>')
# # def heroes_page(series):
# #     character_resp = marvel.get_characters_by_series(series)
# #     name = marvel.random_character_name(character_resp)
# #     return 'welcome to the heroes page.' + name

# @app.route('/heroes/random', methods=['POST', 'GET'])
# def random_heroes_page():
#     print("WTF??!?!??!", request.form)

#     series = request.form.get("series")
#     if series is None:
#         raise Exception("The query param 'series' is required.")
#     # app.logger.info("something", request.form) 
 
#     # return "okay" + series
#     return "okay"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)


    # http://localhost:5000/heroes/random?series=