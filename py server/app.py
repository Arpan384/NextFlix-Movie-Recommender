from flask import Flask, render_template, request, redirect, Response
from flask_cors import CORS, cross_origin
import json
# from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from modules.recommender import recommender
print("Recommender Loaded")

from modules.scrapper import imgScrapper
print("Scrapper Loaded")

@app.route('/server', methods = ['POST'])
@cross_origin()
def worker():
    movie = request.get_json()
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",movie)
    recommended = recommender(movie["name"])
    if type(recommended) == str:
        urlDict = {"message":"Movie Not Found"}
        # print(type(urlDict))
        return json.dumps(urlDict),404

    else:
        urlDict = imgScrapper(recommended)
        # print(type(urlDict))
        return json.dumps(urlDict),200

if __name__ == '__main__':
	app.run(debug=False)

