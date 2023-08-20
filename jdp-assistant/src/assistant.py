from flask import (
    Blueprint,
    render_template)

bp = Blueprint('assistant', __name__, url_prefix="/chat")

VERSION = 'v1'

@bp.route('/', methods=('GET',))
def index():
    try:
        return render_template('assistant/chat.html')
    except:
        return render_template('error.html')