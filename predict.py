import pickle

def prediction(product,mrp,date):
    if(product=='Dairy'):
        regr = pickle.load(open('modelDairy.pkl','rb'))
        output = regr.predict([[mrp,date]])
        return round(output[0],3)

    if(product=='Soft Drink'):
        regr = pickle.load(open('modelSoft Drinks.pkl','rb'))
        output = regr.predict([[mrp,date]])
        return round(output[0],3)

    if(product=='Fruits and Vegetables'):
        regr = pickle.load(open('modelFruits and Vegetables.pkl','rb'))
        output = regr.predict([[mrp,date]])
        return round(output[0],3)

    if(product=='Household'):
        regr = pickle.load(open('modelHousehold.pkl','rb'))
        output = regr.predict([[mrp,date]])
        return round(output[0],3)

    if(product=='Frozen Foods'):
        regr = pickle.load(open('modelFrozen Foods.pkl','rb'))
        output = regr.predict([[mrp,date]])
        return round(output[0],3)

    if(product=='Health and Hygiene'):
        regr = pickle.load(open('modelHealth and Hygiene.pkl','rb'))
        output = regr.predict([[mrp,date]])
        return round(output[0],3)

    if(product=='Snack Foods'):
        regr = pickle.load(open('modelSnack Foods.pkl','rb'))
        output = regr.predict([[mrp,date]])
        return round(output[0],3)