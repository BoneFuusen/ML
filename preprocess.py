import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split

def preprocess(data_file):
    data = pd.read_csv(data_file)
    data["Diabetes_012"] = data["Diabetes_012"].astype(int)
    data["HighBP"] = data["HighBP"].astype(int)
    data["HighChol"] = data["HighChol"].astype(int)
    data["CholCheck"] = data["CholCheck"].astype(int)
    data["BMI"] = data["BMI"].astype(int)
    data["Smoker"] = data["Smoker"].astype(int)
    data["Stroke"] = data["Stroke"].astype(int)
    data["HeartDiseaseorAttack"] = data["HeartDiseaseorAttack"].astype(int)
    data["PhysActivity"] = data["PhysActivity"].astype(int)
    data["Fruits"] = data["Fruits"].astype(int) 
    data["Veggies"] = data["Veggies"].astype(int)
    data["HvyAlcoholConsump"] = data["HvyAlcoholConsump"].astype(int)
    data["AnyHealthcare"] = data["AnyHealthcare"].astype(int)
    data["NoDocbcCost"] = data["NoDocbcCost"].astype(int)
    data["GenHlth"] = data["GenHlth"].astype(int)
    data["PhysHlth"] = data["PhysHlth"].astype(int)
    data["DiffWalk"] = data["DiffWalk"].astype(int)
    data["Sex"] = data["Sex"].astype(int)
    data["Age"] = data["Age"].astype(int)
    data["Education"] = data["Education"].astype(int)
    data["Income"] = data["Income"].astype(int)

    data.drop_duplicates(inplace = True)

    outlier = data[['BMI', 'MentHlth', 'PhysHlth']]
    Q1 = outlier.quantile(0.25)
    Q3 = outlier.quantile(0.75)
    IQR = Q3-Q1

    data_filtered = outlier[~((outlier < (Q1 - 1.5 * IQR)) |(outlier > (Q3 + 1.5 * IQR))).any(axis=1)]

    index_list = list(data_filtered.index.values)

    data_filtered = data[data.index.isin(index_list)]

    data = data_filtered

    y = data["Diabetes_012"]
    X = data.drop(["Diabetes_012"], axis=1)

    scaler = StandardScaler()
    X = scaler.fit_transform(X)


    rus = RandomUnderSampler()
    X_res, y_res = rus.fit_resample(X, y)

    X_train, X_test, y_train, y_test = train_test_split(X_res,y_res,test_size=0.2,random_state=0)

    return X_test, y_test
    