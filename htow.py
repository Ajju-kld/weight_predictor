import pickle

def predict(height):
    model=pickle.load(open('model.pk1','rb'))
    weight=model.predict(height)
    
    return weight[0]

def cm_to_inches(cm):
    inches = float(cm) / 2.54
    return inches

def pounds_to_kg(pounds):
    kg = pounds * 0.45359237
    return kg
