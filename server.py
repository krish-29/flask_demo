
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return 'This is my new page'

if __name__ == '__main__':
    app.run()
