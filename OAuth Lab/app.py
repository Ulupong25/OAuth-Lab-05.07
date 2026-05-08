from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "SECRET_KEY" # Needed for sessions 
oauth = OAuth(app)


# GitHub Configuration
github = oauth.register(
    name='github',
    client_id='Ov23lixXIih6t5jQiGBE',
    client_secret='b28010bc8613a294021abb415f171ace3e192a37',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)


@app.route('/login')
def login():
    # Redirect user to GitHub for authorization
    return github.authorize_redirect(url_for('callback', _external=True))

@app.route('/callback')
def callback():
    # Fetch the token and user info
    token = github.authorize_access_token()
    resp = github.get('user')
    user = resp.json()
    session['user'] = user # Save user to session
    return redirect('/profile')

@app.route('/profile')
def profile():
    # Check if user is logged in
    if 'user' not in session:
        return "Unauthorized", 401
    return jsonify(session['user']) # Show the protected data

@app.route('/logout')
def logout():
    session.pop('user', None) # Remove user from session
    return redirect('/login')

@app.route('/api/secure-data')
def secure_data():
    if 'user' not in session:
        return "Access Denied", 403
    return jsonify({"message": "This is top secret data!", "status": "Success"})

if __name__ == '__main__':
    app.run(debug=True)