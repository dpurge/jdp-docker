import sqlite3

from flask import current_app
from flask import g
from pathlib import Path

def get_database(name):
    if not 'database' in g:
        g.database = {}
    if not name in g.database:
        db_file = Path(current_app.config['DATA_DIR'])/f'{name}.sqlite'
        needs_init = not db_file.is_file()
        db = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES)
        db.row_factory = sqlite3.Row
        if needs_init:
            schema = Path(__file__).resolve().parent/'schema'/f'{name}.sql'
            if not schema.is_file():
                raise RuntimeError('Missing database schema: {schema}')
            db.executescript(schema.read_text('utf-8'))
        g.database[name] = db
    return g.database[name]

def close_database(e=None):
    database = g.pop("database", {})
    for key in database:
        database[key].close()