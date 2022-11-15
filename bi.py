from sklearn import preprocessing
import pandas as pd
dataset = pd.read_csv('Age-salary.csv')
features=dataset.iloc[:,[1]].values
standardscaler_as = preprocessing.Binarizer(threshold=(33))
features_scale = standardscaler_as.fit_transform(features)
dataset['bin-col']=features_scale
print(features_scale)
print(dataset.tail)