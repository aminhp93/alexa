#----------------------------------------- Intent Schema Below:------------------------------

{
  "intents": [
    {
      "intent": "DojoInfoIntent"
    },
    {
      "intent": "DojoStaffIntent"
    },  
    {
      "intent": "AMAZON.HelpIntent"
    },
    {
      "intent": "AMAZON.StopIntent"
    },
    {
      "intent": "DojoStackIntent",
      "slots" : [
        {
          "name": "City",
          "type": "CITIES"
        }
      ]
    },
    {
      "intent" : "TextBrendenIntent"
    },
    {
      "intent" : "GetTouchFaceIntent"
    },
    {
      "intent" : "DojoBrendenIntent"
    },
    {
      "intent" : "AskBrendan"
    },
    {
      "intent" : "twilioIntent"
    }

  ]
}


#----------------------------------------- Utterances Below:------------------------------


DojoInfoIntent what is the coding dojo
DojoInfoIntent tell me about the coding dojo
DojoStaffIntent who are the instructors 
DojoStaffIntent how many instructors work at coding dojo
DojoStackIntent which stacks does {City} teach
TextBrendenIntent Text Brendan
GetTouchFaceIntent Tell what does Brenden say
DojoBrendenIntent who is brenden
AskBrendan what is touchface
twilioIntent text annet



