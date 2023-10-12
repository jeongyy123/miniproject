from flask import Flask, render_template, request, redirect,url_for
#DB 기본 코드
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userEmail = db.Column(db.String(120), unique=True, nullable=False)
    userPw = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'{self.userId} {self.userPw}'

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template('home.html')

# @app.route("/movie/login", methods=["POST"])
# def movie_login():
#     # 폼에서 보낸 데이터 받아오기
#     userEmail_receive = request.form.get("login_userEmail")
#     userPw_receive = request.form.get("login_userPw")
    
#     user = User.query.filter_by(userEmail=userEmail_receive, userPw=userPw_receive).first()
    
#     if user:
#         return redirect(url_for('home'))
#     else:
#         return render_template('movie_login.html')

@app.route('/movie/login')
def movie_login():
    return render_template('login.html')

@app.route("/movie/register")
def movie_register():
    return render_template('register.html')

@app.route("/movie/register/create")
def movie_register_create ():
    #form에서 보낸 데이터 받아오기
    userEmail_receive = request.args.get("userEmail")
    userPw_receive = request.args.get("userPw")

    # 받아온 데이터 => DB 저장하기
    user = User(userEmail=userEmail_receive, userPw=userPw_receive)
    db.session.add(user)
    db.session.commit()

    return render_template('login.html', userEmail=userEmail_receive )

if __name__ == "__main__":
    app.run(debug=True)