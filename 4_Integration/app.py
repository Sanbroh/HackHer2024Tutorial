from flask import Flask, session, render_template, Response, request, request, url_for, flash, redirect, jsonify
import random

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

prompts = []

@app.route('/chat', methods=('GET', 'POST'))
def chat():
    return render_template('chat.html', prompts=prompts)

answers = ["Yes I love money.",
    "Spongebob is a sponge.",
    "You wanna help me make some crabby patties?",
    "Yummers!",
    "Bikini bottom is like my home. I live in it.",
    "Will Smith more like Won't Smith."]

@app.route('/get_response', methods=['GET'])
def get_response():
    if request.method == 'GET':
        rp = request.args["roleplaying"]
        prompt = request.args["msg"]
        print(prompt)
        print(rp)

        r = random.randint(0, 5)

        result = answers[r]

        prompts.append(prompt)
        prompts.append(result)

        return jsonify(result)

if __name__ == "__main__":
  app.run(debug=True)
