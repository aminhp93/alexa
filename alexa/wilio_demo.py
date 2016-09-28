# from flask import Flask, request, redirect
# import twilio.twiml

# app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""

#     resp = twilio.twiml.Response()
#     resp.message("Hello, Mobile Monkey")
#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)


from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC7622914a70ec20b746fa9f5200f94a79"
auth_token = "f61cf7f88337ec156669d6f08ac693cf"
client = TwilioRestClient(account_sid, auth_token)
# 1703209108

message = client.messages.create(to="+18057043552", from_="+16578889320",
                                     body="Hello there!")