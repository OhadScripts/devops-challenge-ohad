from flask import jsonify, Blueprint

health_page = Blueprint('health_page', __name__)


@health_page.route('/health')
def get_secret():
    return jsonify({
        "status": "healthy",
        "container": "link",
        "project": "link"
    })
