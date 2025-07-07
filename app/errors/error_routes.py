from flask import render_template
from app import db

from app.errors import error_blueprint as bp_errors

@bp_errors.app_errorhandler(400)
def bad_request_error(error):
    return render_template('400error.html'), 400

@bp_errors.app_errorhandler(403)
def forbidden_error(error):
    return render_template('403error.html'), 403

@bp_errors.app_errorhandler(404)
def not_found_error(error):
    return render_template('404error.html'), 404

@bp_errors.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500error.html'), 500