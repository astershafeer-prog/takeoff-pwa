from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = 'takeoff-secret-key-2024'

# Simple member data
MEMBERS = [
    {"name": "Ahmed Al Mansoori", "business": "Real Estate Trading", "industry": "Real Estate", "phone": "+971-50-123-4567"},
    {"name": "Priya Krishnan", "business": "Tech Solutions LLC", "industry": "IT Services", "phone": "+971-55-234-5678"},
    {"name": "Mohammed Rashid", "business": "Al Noor Restaurants", "industry": "F&B", "phone": "+971-54-345-6789"},
    {"name": "Sarah Johnson", "business": "Global Import Export", "industry": "Trading", "phone": "+971-52-456-7890"},
    {"name": "Ravi Patel", "business": "Construction Partners", "industry": "Construction", "phone": "+971-50-567-8901"}
]

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/members')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'shafeer' and password == 'demo123':
        session['user'] = username
        return redirect('/members')
    return redirect('/')

@app.route('/members')
def members():
    if 'user' not in session:
        return redirect('/')
    return render_template('members.html', members=MEMBERS)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
