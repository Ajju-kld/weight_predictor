import pickle
import numpy as np
def predict(height):
    model=pickle.load(open('model.pk1','rb'))
    weight=model.predict(height)
    
    return np.array_str(weight)