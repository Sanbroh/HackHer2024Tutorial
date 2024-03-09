from flask import Flask, session, render_template, Response, request, request, url_for, flash, redirect, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == "__main__":
  app.run(debug=True)
