from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.converters import load_data
from rasa_nlu.model import Metadata, Interpreter

interpreter = Interpreter.load("local/models/GatorWatch/default/gw_model", RasaNLUConfig("local/config_spacy.json"))

# @description
#   Give's rasa module our user input and get information about what 
#   it thinks the intents is as well as entities extracted
# @param
#   input (required): the user utterance 
# @return
#   A JSON object that contains each intent and their ranking
#   as well as an array of entities
# @error
#   TypeError if a string is not given
def getInterpretation(input):
    return interpreter.parse(input)