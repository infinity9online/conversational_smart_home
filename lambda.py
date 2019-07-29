from __future__ import print_function
import urllib
import urllib2
import json
import logging
import threading
import uuid
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
""" --- Lex part handler --- """


def dispatch(intent_request):
        
    raise Exception('Intent with name ' + intent_name + ' not supported')


#Main handler

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    try:
        

        if event['request']['type'] == "LaunchRequest":
            return on_launch(event['request'], event['session'])
        elif event['request']['type'] == "IntentRequest":
            return on_intent(event['request'], event['session'])
        elif event['request']['type'] == "SessionEndedRequest":
            return on_session_ended(event['request'], event['session'])
    except:
        
        #logger.debug('event.bot.name={}'.format(event['bot']['name']))
        return dispatch(event)
        

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers

#***************************************************
#first change is here(add the intent name)
#****************************************************

    if intent_name == "distance":
        return run_distance(intent, session)
    elif intent_name == "presence":
        return run_presence(intent, session)
    elif intent_name == "gas":
        return run_gas(intent, session)
    elif intent_name == "light":
        return run_light(intent, session)
    elif intent_name == "ledon":
        return run_ledon(intent, session)
    elif intent_name == "ledoff":
        return run_ledoff(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

#***************************************************
#first change is here(add the intent name)
#****************************************************

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "it was nice interacting with you .thank you . "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# Run the Speed Test

#****************************************************
#Second change is here(add the intent function)
#****************************************************



        
def run_distance(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    #code to update gui
    #print "I am here"
    url = 'https://api.particle.io/v1/devices/190036001547343339383037/ultrasonicvalue/?access_token=f0ba1e9986df1e186b3869138e10b6fe24c89d7f'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    fin = str(resp['result'])
    #print fin
    
    reply="the distance of an object is " + fin + "centimeter" 
    speech_output = reply
                    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def run_presence(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    #code to update gui
    #print "I am here"
    url = 'https://api.particle.io/v1/devices/190036001547343339383037/presence_mess/?access_token=f0ba1e9986df1e186b3869138e10b6fe24c89d7f'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    fin = str(resp['result'])
    #print fin
    
    reply= fin 
    speech_output = reply
                    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_gas(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    #code to update gui
    #print "I am here"
    url = 'https://api.particle.io/v1/devices/190036001547343339383037/gas_mess/?access_token=f0ba1e9986df1e186b3869138e10b6fe24c89d7f'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    fin = str(resp['result'])
    #print fin
    
    reply= fin 
    speech_output = reply
                    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_light(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    url = 'https://api.particle.io/v1/devices/190036001547343339383037/ldr_mess/?access_token=f0ba1e9986df1e186b3869138e10b6fe24c89d7f'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())
    fin = str(resp['result'])
    #print fin
    
    reply= fin 
    speech_output = reply
                    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def run_ledon(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="i have turned on the light ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/190036001547343339383037/led?access_token=f0ba1e9986df1e186b3869138e10b6fe24c89d7f'
    data = urllib.urlencode({'args':'on'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
        
        
        
def run_ledoff(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False
    reply="i have turned off the light ."
    speech_output = reply
    url = 'https://api.particle.io/v1/devices/190036001547343339383037/led?access_token=f0ba1e9986df1e186b3869138e10b6fe24c89d7f'
    data = urllib.urlencode({'args':'off'})
    req = urllib2.Request(url, data)
    req.add_header('content-type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(req)
    resp=json.loads(response.read())

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))        
        





        
#****************************************************
#Second change is here(add the intent function)
#****************************************************

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "this is your smart home skill  . you can ask me various parameters of your home or to control the lights ."

        
    reprompt_text = "sorry i did't got that ."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    
    
    
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
 return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

