import json
from flask import Flask, jsonify, request, Response
from typing import Dict

from ..core import get_podcast_episodes

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello world'



# TODO
# GET that accepts a url and returns info about the podcast 
# and list of episodes (with episode information)
@app.get("/podcast")
def get_podcasts():
    req = request.json 
    if req and isinstance(req, Dict):
        url = req.get('url', '')
    else:
        url = None
    
    if not url:
        return Response("Please send a url of a podcast feed", 400)
    
    try:
    
        info = get_podcast_episodes(url)

        response = {
            'message': f'Here is your podcast information from {url}',
            'data': info,
        }

        return Response(json.dumps(response), 200)
    except Exception as error:
        e = f"An error was encountered when processing your request - {error}"
        args = {
            "msg": e,
        }
        return Response(json.dumps(args), 400)

if __name__ == "__main__":
    app.run()