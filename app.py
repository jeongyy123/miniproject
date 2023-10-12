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

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ott = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    period = db.Column(db.String(100), nullable=False)
    contents = db.Column(db.String(10000), nullable=False)

#    def __repr__(self):
#        return f'{self.userId} {self.userPw}'

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

@app.route("/board/")
def board():
    board_list = Board.query.all()
    return render_template('board_list.html', data=board_list)

@app.route("/board/write/")
def board_detail():
    return render_template('board_write.html')

@app.route("/board/view/<board_id>")
def board_view(board_id):
    board_detail = Board.query.filter_by(id=board_id).first()
    print(board_detail.ott)
    return render_template('board_view.html', data=board_detail)

@app.route('/board/create/', methods=['POST'])
def board_create():
    ott_receive = request.form.get('ott_select')
    title_receive = request.form.get("title")
    price_receive = request.form.get("price_select")
    period_receive = request.form.get("period_select")
    contents_receive = request.form.get("contents")
    
    board = Board(ott=ott_receive, title=title_receive, price=price_receive, period=period_receive, contents=contents_receive)
    db.session.add(board)
    db.session.commit()
    return redirect(url_for('board'))

if __name__ == "__main__":
    app.run(debug=True)
