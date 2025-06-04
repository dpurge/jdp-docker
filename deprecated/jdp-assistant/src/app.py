import os
from flask import Flask
from pathlib import Path
from database import close_database
# from dotenv import load_dotenv


import authentication
import page
import assistant

# load_dotenv()

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = os.environ.get("SECRET_KEY", 'development'),
    DATA_DIR = os.environ.get("DATA_DIR", str(Path(__file__).resolve().parent.parent / 'data'))
)

app.register_blueprint(authentication.bp)
app.register_blueprint(page.bp)
app.register_blueprint(assistant.bp)
app.teardown_appcontext(close_database)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)