from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello world'



# TODO
# GET that accepts a url and returns info about the podcast 
# and list of episodes (with episode information)
@app.get("/podcast")
def get_podcasts():
    url = request.json.__dict__.get('url', '')

    if not url:
        # TODO send appropriate status codes
        return "Please send a url of a podcast feed"
    
    # TODO use url to get podcast info

    return 'Here is your podcast infor'

if __name__ == "__main__":
    app.run()