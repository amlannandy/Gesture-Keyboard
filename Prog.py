from __future__ import print_function
from pygarl.base import CallbackManager
from pygarl.classifiers import SVMClassifier
from pygarl.mocks import VerboseMiddleware
from pygarl.data_readers import SerialDataReader
from pygarl.predictors import ClassifierPredictor
from pygarl.sample_managers import DiscreteSampleManager

MODEL_PATH="C:\Users\Lenovo\Documents\Gesture Keyboard\model.svm"
PORT="COM8"

def receive_character(character):
    f = open("test.txt",'a+')
    f.write(character)
    print("........................"+character)


sdr = SerialDataReader(PORT, expected_axis=6, verbose=False)

manager = DiscreteSampleManager()

sdr.attach_manager(manager)


classifier = SVMClassifier(model_path=MODEL_PATH)

classifier.load()

classifier.print_info()

predictor = ClassifierPredictor(classifier)

manager.attach_receiver(predictor)

callback_mg = CallbackManager(verbose=True)

predictor.attach_callback_manager(callback_mg)

for c in ["are", "team merlin at cisco thingqbator", " ", ".", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    callback_mg.attach_callback(c, receive_character)

sdr.open()
print("Opened!")
sdr.mainloop()
