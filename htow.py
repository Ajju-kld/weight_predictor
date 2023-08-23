import pickle

def predict(height):
    model=pickle.load(open('model.pk1','rb'))
    weight=model.predict(height)
    
    return weight[0]