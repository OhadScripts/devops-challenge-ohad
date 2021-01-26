from SecretController import secret_page
from flask import Flask


def main():
    app = Flask(__name__)
    app.register_blueprint(secret_page)
    app.run()


if __name__ == "__main__":
    main()
