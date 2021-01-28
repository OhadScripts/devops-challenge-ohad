from flask import jsonify, Blueprint
from HealthService import Health

health_page = Blueprint('health_page', __name__)
health = Health()


@health_page.route('/health')
def get_secret():
    return jsonify(health.get_health_shot())
