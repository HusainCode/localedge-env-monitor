from flask import Flask, render_template
from dotenv import load_dotenv
from routes import routes, main
import os

load_dotenv()

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    app.register_blueprint(main)
    app.register_blueprint(routes)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0") # 0.0.0.0 for remote access
