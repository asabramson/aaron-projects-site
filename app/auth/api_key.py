# This function can be added as a decorator to routes to block unauthorized POST requests without an API key
# The API key should be specified as 'API_KEY' in your .env file
# This function is not in use yet, CSRF protection is used to protect the routes from malicious requests. I do have a project idea that I will start on soon that will use this!

from functools import wraps
from flask import request, abort, current_app

def api_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        server_api_key = current_app.config.get('API_KEY')
        
        submitted_key = request.headers.get('X-API-Key')
        
        if not submitted_key or submitted_key != server_api_key:
            abort(401, description="Unauthorized: Invalid or missing API key.")
            
        return f(*args, **kwargs)
    return decorated_function