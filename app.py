from flask import Flask, make_response
from requests import get

app = Flask(__name__)

API_URL   = 'https://api.mojang.com/users/profiles/minecraft/%s'
SKINS_URL = 'http://skins.voxelmodpack.com/skins/%s.png'

def get_profile(nickname):
    r = get(API_URL % nickname)
    return None if r.status_code == 204 else r.json()

def cors_response(content, code):
    if type(content) is str:
        content = content.encode('utf-8')
    
    response = make_response(content)
    response.status_code = code
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Expose-Headers', 'X-Nickname')
    return response

@app.route('/')
def index():
    return cors_response('No nickname provided', 400)

@app.route('/<string:nickname>')
def get_skin(nickname):
    profile = get_profile(nickname)
    if profile:
        r = get(SKINS_URL % profile.get('id'))
        if r.status_code == 404: return cors_response('No skin for nickname "%s"' % profile.get('name'), 404)
        
        response = cors_response(r.content, 200)
        response.headers.set('X-Nickname', profile.get('name'))
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'inline; filename="%s.png"' % profile.get('name'))
        return response
    else:
        return cors_response('No profile for nickname "%s"' % nickname, 404)
