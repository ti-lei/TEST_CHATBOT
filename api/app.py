from flask import Flask, request, abort
from urllib.parse import parse_qsl

from events import basic
# from events.service import *
# from line_bot_api import *

# from extensions import db, migrate
# from models.user import User
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"