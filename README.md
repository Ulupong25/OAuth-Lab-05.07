Lab 05.07: Securing APIs using OAuth 2.0 with GitHub and Auth0 
Project Overview
This project demonstrates how to secure a Flask API using OAuth 2.0 and GitHub. It validates user identity through GitHub's authorization server to protect sensitive endpoints.

Quick Start
Install Dependencies:

Bash
pip install flask authlib requests
Configure Credentials:
Update client_id and client_secret in app.py with your GitHub Developer settings.

Run App:

Bash
python app.py
Access:
Navigate to http://127.0.0.1:5000/login.

Protected Routes
/profile: Returns user JSON data (Requires Login).

/api/secure-data: Bonus route returning encrypted-style status (Requires Login).

/logout: Clears the session.

Key Concepts
The application follows the Authorization Code Flow, ensuring the server never sees your GitHub password.

Repository Structure
app.py: Main application code.

requirements.txt: Project dependencies.

/screenshots: Visual proof of successful authentication and protected access.
