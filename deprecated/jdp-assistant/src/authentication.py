import functools

from flask import (
    Blueprint,
    flash,
    g,
    jsonify,
    request,
    redirect,
    render_template,
    session,
    url_for)
from werkzeug.security import (
    check_password_hash,
    generate_password_hash)
from database import get_database


bp = Blueprint('authentication', __name__, url_prefix="/auth")
api = 'v1'


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        if not error:
            db = get_database(name='app-cfg')
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("authentication.login"))
        flash(error)
    return render_template('authentication/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        db = get_database(name='app-cfg')
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        if not error:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('page.index'))
        flash(error)
    return render_template('authentication/login.html')


@bp.before_app_request
def load__user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_database(name='app-cfg').execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('page.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('authentication.login'))

        return view(**kwargs)

    return wrapped_view


@bp.route('/profile')
@login_required
def profile():
    return render_template('authentication/profile.html')


@bp.route(f'/{api}/profile')
@login_required
def get_profile():
    return jsonify({
        'id': g.user['id'],
        'username': g.user['username'],
    })