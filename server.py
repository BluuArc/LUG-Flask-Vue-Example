from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__,static_url_path='/static/', static_folder='sample-client/dist')

CORS(app)

@app.route('/')
def hello_world():
  return app.send_static_file('index.html')

@app.route('/static/<path:path>')
def sendStatic(path):
  return app.send_static_file(path)

@app.route('/api')
def appRoot():
  return 'API response here!'

def makeMockPost(title, content):
  post = dict()
  post['title'] = title
  post['content'] = content
  return post

@app.route('/api/posts')
def getPosts():
  posts = [
    makeMockPost('Test post', 'Test post. Please Ignore'),
    makeMockPost('First post', 'This is the first, non-test post'),
    makeMockPost('Foo?', 'Bar.'),
  ]
  return jsonify(posts)

