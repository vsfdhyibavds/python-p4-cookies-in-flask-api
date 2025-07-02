# Running and Testing the Flask API with Cookies and Sessions

## Setup

1. Ensure you have Python 3.7+ installed.

2. Install dependencies and activate the virtual environment using pipenv:

```
pipenv install
pipenv shell
```

## Running the Flask App

Run the Flask app with:

```
python server/app.py
```

The app will start on port 5555.

## Testing the /sessions/<key> Endpoint

1. Open your browser or use an HTTP client (e.g., Postman, curl).

2. Make a GET request to:

```
http://localhost:5555/sessions/hello
```

3. You should receive a JSON response containing:

- Session data with keys "hello" and "goodnight".
- Cookies sent by the client.
- A cookie named "mouse" set in the response.

## Inspecting Cookies

- In your browser, open Developer Tools.
- Go to the Application tab (or Storage).
- Find the Cookies section for `http://localhost:5555`.
- You can view and edit cookies here.
- Refresh the page to see updated cookie values.

## Notes

- The session cookie is signed and encrypted by Flask, so it cannot be tampered with.
- The "mouse" cookie is a simple cookie set by the server.
- The session persists until the browser is closed or the session expires.
