from uuid import uuid4
from flask import Blueprint,render_template, flash, redirect, url_for, request, jsonify, session

from app import db
from app.main.lasker_morris import laskermorris_blueprint as bp_lm
from app.main.lasker_morris import lasker_morris_player as aip



GAMES = {}

def _sid():
    if 'sid' not in session:
        session['sid'] = str(uuid4())
    return session['sid']

def _new_state():
    s = aip.initial_state()
    return s

def _from_frontend(src, dest, rem, player='blue'):
    # Standardize mapping to the format that the AI player program uses (differs slightly from the frontend)
    if src == 'h':
        src = 'h1' if player == 'blue' else 'h2'
    rem = 'r0' if (not rem or rem == 'r') else rem
    return (src, dest, rem)

def _to_frontend(ai_move):
    # Standardize mapping (again)
    if not ai_move:
        return None
    src, dest, rem = ai_move
    if src in ('h1', 'h2'):
        src = 'h'
    if rem == 'r':
        rem = 'r0'
    return {'source': src, 'dest': dest, 'removal': rem}

@bp_lm.route('/laskermorris', methods=['GET'])
def laskermorris():
    # Reset the user's game whenever they open/refresh the page
    sid = _sid()
    state = aip.initial_state()
    # Set user's color to blue so the AI always expects orange (sets player1 and player2)
    state['turn'] = 'blue'
    GAMES[sid] = state
    return render_template('lasker_morris.html', title="Lasker Morris")

@bp_lm.route('/move', methods=['POST'])
def move():
    sid = _sid()
    # Create new if not already existing
    state = GAMES.get(sid) or _new_state()

    data = request.get_json()
    src = data['source']
    dest = data['dest']
    removal = data.get('removal', 'r0')

    # Apply user's move to AI state
    user_move = _from_frontend(src, dest, removal, player='blue')
    state = aip.apply_move(state, user_move)

    if aip.is_terminal_frontend(state):
        GAMES[sid] = state
        return jsonify({'aiMove': None, 'gameOver': True})

    # Query AI for move based on given game state
    ai_move = aip.iterative_deepening(state, player='orange')
    if ai_move is not None:
        state = aip.apply_move(state, ai_move)

    # Alternative to original global variable storage option (which is not recommended for production Flask projects!)
    GAMES[sid] = state

    return jsonify({
        'aiMove': _to_frontend(ai_move),
        'gameOver': aip.is_terminal_frontend(state)
    })