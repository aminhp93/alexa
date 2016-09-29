#----------------------------------------- Intent Schema Below:------------------------------

{
    "intents": [
        {
            "intent": "AMAZON.ResumeIntent"
        },
        {
            "intent": "AMAZON.PauseIntent"
        },
        {
            "intent": "DojoInfoIntent"
        },
        {
            "intent": "AMAZON.HelpIntent"
        },
        {
            "intent": "AMAZON.StopIntent"
        },
        {
            "intent": "TextBrendenIntent"
        },
        {
            "intent": "GetTouchFaceIntent"
        },
        {
            "intent": "DojoBrendenIntent"
        },
        {
            "intent": "AskBrendan"
        },
        {
            "intent": "twilioIntent"
        },
        {
            "intent": "GroupTextIntent",
            "slots": [
                {
                    "name": "Name",
                    "type": "MEMBERS"
                }
            ]
        }
    ]
}

#----------------------------------------- Utterances Below:------------------------------

DojoInfoIntent what is the coding dojo
DojoInfoIntent tell me about the coding dojo
TextBrendenIntent Text Brendan
GetTouchFaceIntent Tell what does Brenden say
DojoBrendenIntent who is brenden
AskBrendan what is touchface
twilioIntent hi annet
GroupTextIntent text {Name}



