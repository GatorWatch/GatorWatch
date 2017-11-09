from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.converters import load_data

trainingData = load_data("local/data/testData.json")
trainer = Trainer(RasaNLUConfig("local/config_spacy.json"))
trainer.train(trainingData)
modelDirectory = trainer.persist("local/models/GatorWatch/")