from flask import Flask, request, session, render_template
app = Flask(__name__)

@app.route('/')
def index(): pass
    #return '상자아이의 웹페이지 1'
@app.route('/hello/')
def hello():
    return 'Hello World!'

@app.route('/user/<username>/')
def show_user_profile(username):
#유저 이름을 보여줌
    #app.logger.debug('RETRIEVE DATA - USER ID : %s' % username)
    #app.logger.debug('RETRIEVE DATA - Check Compelete')
    return  'User %s' % username
#with app.test_request_context():
    #print url_for('index')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')

