import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
def predict(data):
    # Load the model
    model = pickle.load(open('elastic_net.pkl', 'rb'))
    # Make prediction
    result = model.predict(data)
    return result