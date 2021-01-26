from flask import jsonify, Blueprint
from SecretService import Database
from os import getenv
from dotenv import load_dotenv

secret_page = Blueprint('secret_page', __name__)

load_dotenv()
client = Database(getenv("AWS_ACCESS_KEY_ID"),
                  getenv("AWS_SECRET_ACCESS_KEY"),
                  getenv("REGION_NAME"))


@secret_page.route('/secret')
def get_secret():
    return jsonify(client.secret)
