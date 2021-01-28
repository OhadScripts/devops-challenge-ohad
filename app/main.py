from SecretController import secret_page
from HealthController import health_page
from flask import Flask

app = Flask(__name__)
app.register_blueprint(secret_page)
app.register_blueprint(health_page)


def main():
    app.run()


if __name__ == "__main__":
    main()
