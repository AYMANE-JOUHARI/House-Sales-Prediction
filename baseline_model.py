import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

train_data = pd.read_csv('data/train.csv')
validation_data = pd.read_csv('data/validation.csv')
X_train = train_data.drop(columns=['sale_price', 'house_id', 'sale_date'])
y_train = train_data['sale_price']
X_val = validation_data.drop(columns=['house_id', 'sale_date'])
house_ids = validation_data['house_id']

categorical_cols = ['city', 'house_type']
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['months_listed', 'bedrooms', 'area']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_val)
base_result = pd.DataFrame({
    'house_id': house_ids,
    'price': predictions.round(2)
})
base_result.to_csv("base_result.csv", index=False)
print("Baseline model predictions saved.")