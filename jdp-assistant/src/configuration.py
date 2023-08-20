from flask import (
    Blueprint,
    render_template)
from authentication import login_required

bp = Blueprint('configuration', __name__, url_prefix="/cfg")

VERSION = 'v1'

@bp.route('/script', methods=('GET',))
@login_required
def script():
    try:
        return render_template('configuration/script.html')
    except:
        return render_template('error.html')

@bp.route('/language', methods=('GET',))
@login_required
def language():
    try:
        return render_template('configuration/language.html')
    except:
        return render_template('error.html')