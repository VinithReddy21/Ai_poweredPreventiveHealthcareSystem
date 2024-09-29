import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Connect to the SQLite database
conn = sqlite3.connect('health_data.db')

# Load data into a pandas DataFrame
query = 'SELECT blood_pressure, exercise_hours, diet FROM user_data'
data = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Convert diet to numerical values
data['diet'] = data['diet'].map({'balanced': 0, 'high_sugar': 1, 'low_carb': 2})

# Display the first few rows of the data
print(data.head())



# Define features and target variable
X = data[['exercise_hours', 'diet']]
y = (data['blood_pressure'] >= 130).astype(int)  # Binary target: 1 for high blood pressure, 0 otherwise


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Initialize and train the model
model = LogisticRegression()
model.fit(X_train, y_train)



# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)




# Example new data for prediction
new_data = pd.DataFrame({
    'exercise_hours': [3],  # Example exercise hours
    'diet': [1]              # Example diet type (high_sugar)
})

# Predict the risk
prediction = model.predict(new_data)
risk = 'High' if prediction[0] == 1 else 'Normal'
print(f'Risk of high blood pressure: {risk}')
