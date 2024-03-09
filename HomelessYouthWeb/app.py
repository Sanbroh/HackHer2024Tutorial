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

answers = [
    #Where can I find a local food shelter near me?
    "You can find a local food shelter near you at Partners in Mission Food Bank, located at 140 Hickson Avenue in Kingston, Ontario. They are open Monday to Friday from 8:30 AM to 4:00 PM and can be reached at (613) 544-4534 for more information.",
    #How can I help unhoused youth as a student?
    "As a student, there are several ways you can help unhoused youth in Kingston, Ontario. You can volunteer your time at organizations like the Kingston Youth Shelter or Youth Diversion, offering mentorship, tutoring, or recreational activities. Additionally, you can raise awareness about youth homelessness through events or fundraisers, and consider donating essential items or funds to local shelters.",
    #"I'm scared of not making rent and I can barely afford groceries, I need help and support
    "If you're facing difficulties with rent and affording groceries, you can seek assistance from the Kingston Food Bank. They provide food assistance to individuals in need and may also offer support for housing-related issues. You can visit their location at 140 Hickson Avenue, Kingston, Ontario, during their operating hours or contact them through their website for further assistance. Additionally, you can find their phone number listed on their website for direct contact."    "Yummers!",
    #My home isn't safe and I need a place to stay tonight
    "If you're in need of a safe place to stay tonight due to an unsafe home environment, you can seek assistance from Kingston Interval House. They provide shelter and support for individuals experiencing domestic violence. You can contact them at their helpline: (613) 546-1833, available 24/7, or visit their location at 237 Wellington Street, Kingston, Ontario, for immediate assistance. Additionally, you can access their phone number through their website for further inquiries.",
    #Where can i donate to help at risk youth
    "If you're looking to donate to support at-risk youth in Kingston, you can consider reaching out to organizations like Kingston Youth Shelter. They provide various services and support to youth experiencing homelessness or at risk of homelessness. You can contact them at their location: 234 Brock Street, Kingston, Ontario, during their operating hours, or find their phone number on their website for further information on how you can contribute to their cause."]

@app.route('/get_response', methods=['GET'])
def get_response():
    if request.method == 'GET':
        rp = request.args["roleplaying"]
        prompt = request.args["msg"]
        print(prompt)
        print(rp)

        r = 0 #random.randint(0, 5)

       result = answers[r]

        r = (r+1) % 5
        prompts.append(prompt)
        prompts.append(result)

        return jsonify(result)

if __name__ == "__main__":
  app.run(debug=True)
