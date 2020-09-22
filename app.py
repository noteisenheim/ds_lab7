from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    frogs = ['bullfrog', 'wood frog', 'cane toad', 'squeeking frog']
    frog = random.choice(frogs)

    return render_template('index.html', frog=frog)

@app.route('/other')
def other():
    return render_template('other.html')

@app.route('/signup')
def signup():
    return render_template('signin.html')

@app.route('/thanks')
def thanks():
    name = request.args.get('name')
    return render_template('thanks.html', name=name)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')