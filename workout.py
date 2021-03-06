from flask import Flask,render_template, request, url_for, session
from model import db, User
import bcrypt
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone!'
"""
flask_bcrypt = Bcrypt(app)
"""
@app.route('/')
def index():
    return render_template('index.html')

app.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(name=request.form['username'].encode('utf-8')).first()

    if user is not None:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), user.password.encode('utf-8')) == user.password.encode('utf-8'):
            session['username'] = request.form['username']
            return url_for('index')
        return 'password is incorrect' 
    
    
    return 'User does not exist!'


if __name__=='__main__':
    app.run(debug=True)