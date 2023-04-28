import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    try:
        from chatterbot import ChatBot
        from chatterbot.trainers import ListTrainer
    except:
        return "Please install ['chatterbot'] python packages for the chatbot to work."
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        # TODO Add code here
        # Create a new chat bot named Charlie
        chatbot = ChatBot('Charlie')

        trainer = ListTrainer(chatbot)

        trainer.train([
            "Hi",
            "How to build a scientific chatbot?",
            "Here is the steps."
        ])

        # Get a response to the input text 'How to develop a scientific chatbot?'
        response = chatbot.get_response('How to develop a scientific chatbot?')        
        
        #response = ''
        output.append(response)

    return SimpleText(dict(text=output))
