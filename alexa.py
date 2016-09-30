import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

from twilio.rest import TwilioRestClient

print("I AM RIGHT HERE AT THE TOP OF THE FILE")

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

# --------------------Dont touch below!--------------------------
@ask.launch

def launch_skill():

    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("DojoInfoIntent")

def dojo_info():
    response = render_template("dojo_info_template")
    return statement(response)



@ask.intent("AMAZON.HelpIntent")

def dojo_help():
    response = render_template("help_template")
    return question(response)
#--------OK Above-----------


# @ask.intent("DojoStackIntent", convert={'City': str})

# def dojo_stacks(City):
#     response = ''
#     if City == "San Jose":
#         response = render_template("san_jose_stacks", city=City)
#     elif City == "Seattle":
#         response = render_template("seattle_stacks", city=City)
#     elif City == "Chicago":
#         response = render_template("chicago_stacks", city=City)
#     elif City == "Dallas":
#         response = render_template("dallas_stacks", city=City)
#     elif City == "Burbank":
#         response = render_template("burbank_stacks", city=City)
#     elif City == "Washington":
#         response = render_template("washington_stacks", city=City)
#     else:
#         response = render_template("invalid_city")

#     return statement(response)
#-----------------------Ok above----------
#--------------Custom functions below--------

@ask.intent("TextBrendenIntent")
def touch_face_with_Brenden():
    print("I AM RIGHT HERE")
    response = render_template("brendan_template_1")
    return statement(response)


@ask.intent("GetTouchFaceIntent")
def get_touchface_response():
    response = render_template("brendan_template_2")
    return statement(response)

@ask.intent("DojoBrendenIntent")
def dojo_Brenden_response():
    response = render_template("brendan_template_3")
    return statement(response)

@ask.intent("AskBrendan")
def ask_brendan():
    response = render_template("brendan_template_4")
    return statement(response)


@ask.intent("twilioIntent")

def twilioIntentHandler():

    account_sid = "AC7622914a70ec20b746fa9f5200f94a79"
    auth_token = "f61cf7f88337ec156669d6f08ac693cf"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to="+15103646406", from_="+16578889320", body="Hey Brendan, I touch your face lol!!!!")
    response = render_template("message_sent_to")
    return question(response)


@ask.intent("GroupTextIntent", convert={'Name': str})

def GroupTextIntentHandler(Name):

    account_sid = "AC7622914a70ec20b746fa9f5200f94a79"
    auth_token = "f61cf7f88337ec156669d6f08ac693cf"
    client = TwilioRestClient(account_sid, auth_token)

    if Name == "Andy":
        message = client.messages.create(to="+18057043552", from_="+16578889320", body="Hello Andy you are doing well today!")
        response = render_template("message_sent", name = Name)
    elif Name == "Annet":
        message = client.messages.create(to="+15102142298", from_="+16578889320", body="Hello Annet you are doing well today!")
        response = render_template("message_sent", name = Name)
    elif Name == "Luba":
        message = client.messages.create(to="+17032091080", from_="+16578889320", body="Hello Tuba you are doing well today!")
        response = render_template("message_sent", name = Name)
    elif Name == "Minh":
        message = client.messages.create(to="+17142135025", from_="+16578889320", body="Hello Minh you are doing well today!")
        response = render_template("message_sent", name = Name)
    else:
        response = render_template("message_not_sent")
    return question(response)
    


if __name__ == '__main__':

    app.run(debug=True)
