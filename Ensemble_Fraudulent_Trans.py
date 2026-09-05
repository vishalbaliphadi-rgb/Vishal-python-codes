import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,f1_score,recall_score,classification_report

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

#Step1: Load the Dataset

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print ("Shape of Dataset: ", df.shape)

print ("First Few Records: ")
print (df.head())
print (df.tail())

# Step-2 : Seperate Features and Labels

X = df.drop("Fraud",axis=1)
Y = df["Fraud"]

print ("X Shape: ", X.shape)
print ("Y Shape: ", Y.shape)

# Step-3: Split Dataset for Training and Testing

X_train, X_test , Y_train, Y_test = train_test_split (X, Y, random_state= 42, test_size= 0.2)

# Step-4 : Scale the Feature

scalar = StandardScaler()

X_train = scalar.fit_transform (X_train)
X_test = scalar.fit_transform (X_test)

# Step 5.1 Create the Individual Models

model_det = DecisionTreeClassifier (random_state=42)
model_bag = BaggingClassifier (random_state=42,n_estimators= 10)
model_ranForest = RandomForestClassifier (random_state= 42, n_estimators=10)
model_adaboost = AdaBoostClassifier (n_estimators=50, learning_rate= 1.0, random_state=42)

# Step 5.2 Create Voting Model

model = VotingClassifier(
    estimators= [
                 ('decision_tree',model_det),
                  ('bagging', model_bag),
                  ('random_forest', model_ranForest),
                  ('adaboost', model_adaboost)
                 
                 ],
                 voting= 'soft'

)

# Step-6: Train the Model

model = model.fit (X_train, Y_train)

# Step-7: Test the model

Y_pred = model.predict (X_test)

# Step-8 : Evaluate the model

print ("Accuracy: ", accuracy_score(Y_test,Y_pred))
print ("Confusion Matrix: ", confusion_matrix(Y_test,Y_pred))
print ("precision: ", precision_score(Y_test,Y_pred))
print ("F1 Score: ", f1_score(Y_test,Y_pred))
print ("Recall: ", recall_score(Y_test,Y_pred)) 
print ("Classification Report: \n", classification_report(Y_test,Y_pred))




