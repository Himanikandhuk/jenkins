from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Simulating a simple in-memory user storage (use a database in production)
users = {}

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Check if the user already exists
    if username in users:
        flash('Username already exists. Try another one.')
        return redirect(url_for('home'))

    # Add user to the in-memory storage
    users[username] = {'email': email, 'password': password}
    flash('Registration successful! You can now log in.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=True)

