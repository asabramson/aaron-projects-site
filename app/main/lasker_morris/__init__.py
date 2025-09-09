from flask import Blueprint

laskermorris_blueprint = Blueprint('lm', __name__)

from app.main.lasker_morris import lm_routes