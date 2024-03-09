from flask import Flask, session, render_template, Response, request, request, url_for, flash, redirect, jsonify
import random
import os
import openai

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

os.environ["OPENAI_API_KEY"] = 'put_your_secret_key_here!'
openai.api_key = os.getenv("OPENAI_API_KEY")

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

def getNarratorResponse(prompt, roleplaying):
    narratorResponse = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You will roleplay as Mr. Krabs in from spongebob squarepants and will respond to prompts as him in character"},
        {"role": "assistant", "content": "You are speaking to " + str(roleplaying) + ", so respond as if you are talking to him."},
        {"role": "user", "content": "Being Mr. Krabs, give a response to the user saying '" + prompt + ". The response is what Mr. Krabs would say" + ". Make this one to four sentences response. Do not mention that you are Mr. Krabs in the response, and be objective, providing no bias, and only the response. When referencing the user, refer to them as who they are and not as a random character using the third-person perspective. Always and only provide the reply from as Mr. Krabs. If you cannot provide a response, then just say you have no opinions on this topic."}
    ]
    ).choices[0].message.content

    print(narratorResponse)
    response = narratorResponse

    try:
        response = re.findall('"(\D+)"', response)[0]
    except:
        response = response

    return response

@app.route('/get_response', methods=['GET'])
def get_response():
    if request.method == 'GET':
        rp = request.args["roleplaying"]
        prompt = request.args["msg"]
        print(prompt)
        print(rp)

        result = getNarratorResponse(prompt, rp)

        prompts.append(prompt)
        prompts.append(result)

        return jsonify(result)

def generateTTS(file_name, prompt):
    speech_file_path = f"./static/audio/{file_name}.mp3"
    print(speech_file_path)

    # TTS
    response = openai.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input=prompt
    )

    #writes to file
    with open(speech_file_path, "wb") as f:
        f.write(response.content)

    return "Success in creating audio!"

@app.route('/get_tts', methods=['GET'])
def get_tts():
    if request.method == 'GET':
        prompt = request.args["msg"]
        file_name = request.args["filename"]
        result = generateTTS(file_name, prompt)

        return jsonify(result)

if __name__ == "__main__":
  app.run(debug=True)
