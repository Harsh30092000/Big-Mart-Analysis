import pandas as pd
from sklearn import linear_model
import pickle


data = pd.read_csv('train.csv')
data.head(11)


item_type = list(data["Item_Type"])
item_mrp = list(data["Item_MRP"])
year = list(data["Outlet_Establishment_Year"])
sales = list(data["Item_Outlet_Sales"])



my_data = {}
all_types = set(item_type)

for i in all_types:
    my_data[i] = []
    mrp_l = []
    year_l = []
    sales_l = []
    for j in range(len(item_type)):
        if(item_type[j]==i):
            mrp_l.append(item_mrp[j])
            year_l.append(year[j])
            sales_l.append(sales[j])
    my_data[i].append(mrp_l)
    my_data[i].append(year_l)
    my_data[i].append(sales_l)




for i in all_types:

    data_set = {'Mrp': my_data[i][0],
                'Year': my_data[i][1],
                'Sales': my_data[i][2]
                }

    df = pd.DataFrame(data_set,columns=['Mrp','Year','Sales'])

    X = df[['Mrp','Year']]
    Y = df['Sales']
    
    # with sklearn
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)

    print('Intercept: \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)
    file_name = "model" + i + ".pkl"
    pickle.dump(regr, open(file_name,'wb'))