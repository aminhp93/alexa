import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


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


@ask.intent("DojoStackIntent", convert={'City': str})

def dojo_stacks(City):
    response = ''
    if City == "San Jose":
        response = render_template("san_jose_stacks", city=City)
    elif City == "Seattle":
        response = render_template("seattle_stacks", city=City)
    elif City == "Chicago":
        response = render_template("chicago_stacks", city=City)
    elif City == "Dallas":
        response = render_template("dallas_stacks", city=City)
    elif City == "Burbank":
        response = render_template("burbank_stacks", city=City)
    elif City == "Washington":
        response = render_template("washington_stacks", city=City)
    else:
        response = render_template("invalid_city")

    return statement(response)
#-----------------------Ok above----------
#--------------Custom functions below--------

@ask.intent("TextBrendenIntent")
def touch_face_with_Brenden():
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




if __name__ == '__main__':

    app.run(debug=True)
