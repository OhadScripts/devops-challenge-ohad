from SecretController import secret_page
from flask import Flask

app = Flask(__name__)
app.register_blueprint(secret_page)


def main():
    app.run()


if __name__ == "__main__":
    main()
