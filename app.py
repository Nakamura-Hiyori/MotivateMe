import os
from flask import (
    Flask,
    jsonify,
    render_template)
from flask_cors import CORS
from model1 import cheer

# インスタンス化する
app = Flask(__name__) #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く
CORS(app)

#ルーティング設定をする
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cheer')
def cheer_get():
    return render_template('1_cheer.html')

@app.route('/praise')
def praise_get():
    return render_template('2_praise.html')

@app.route('/love')
def love_get():
    return render_template('3_love.html')

@app.route('/cheerdata')
def get_cheerdata():
    cheerdata = cheer()
    return jsonify(cheerdata)

@app.route('/praisedata')
def get_praisedata():
    praisedata = cheer()
    return jsonify(praisedata)

@app.route('/lovedata')
def get_lovedata():
    lovedata = cheer()
    return jsonify(lovedata)

if __name__ == "__main__":
    app.run(debug=True)

