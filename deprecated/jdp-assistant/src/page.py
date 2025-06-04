from flask import Blueprint
from flask import render_template

bp = Blueprint('page', __name__)

VERSION = 'v1'

@bp.route('/', methods=('GET',))
def index():
    try:
        return render_template('page/index.html')
    except:
        return render_template('error.html')