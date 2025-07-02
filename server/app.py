
from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False

# Secret key for signing the session cookie
app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    """
    Endpoint to demonstrate working with Flask sessions and cookies.
    Sets default session values if not present, returns session and cookie data,
    and sets a cookie in the response.
    """
    # Set default session values if not already set
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Check if the requested key exists in the session
    if key not in session:
        return jsonify({'error': f'Session key "{key}" not found.'}), 404

    # Prepare JSON response with session and cookie data
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
            for cookie in request.cookies],
    }), 200)

    # Set a cookie named 'mouse' with value 'Cookie'
    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    # Run the Flask app on port 5555
    app.run(port=5555)
