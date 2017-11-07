from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.converters import load_data
from rasa_nlu.model import Metadata, Interpreter

interpreter = Interpreter.load("local/models/GatorWatch/default/model_20171106-093358", RasaNLUConfig("local/config_spacy.json"))

def determineIntent(input):    
    result = interpreter.parse(input)
    return result["intent"]["name"]