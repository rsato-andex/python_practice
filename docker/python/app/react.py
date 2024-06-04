from flask import Blueprint, send_from_directory, session, jsonify

react = Blueprint('react', __name__, static_folder='static/build')

@react.route('/')
def serve():
    return send_from_directory(react.static_folder, 'index.html')

@react.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(react.static_folder, path)

@react.route('/api/session')
def get_session():
    return jsonify({'username': session.get('username', '')})
