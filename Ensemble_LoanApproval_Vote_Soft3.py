import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier


##############################################################################################
# Step-1 : Load the data
##############################################################################################

br = "="*40

df = pd.read_csv("Customer_Loan_Approval.csv")

print ("Data Load successful")

print (br)
print ("Initial few records from Dataset\n", df.head())
print (br)

##############################################################################################
# Step-2: Check for Missing values
##############################################################################################

print ("Check Missing Values")
print (df.isnull().sum())

#############################################################################################
# Step-3: Seperate Input and Output variables
############################################################################################

X = df.drop("LoanApproved", axis = 1)
Y = df["LoanApproved"]

print ("X Shape", X.shape)
print ("Y Shape", Y.shape)

##########################################################################################
# Step-4: Split dataset into training and testing
##########################################################################################

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print ("Splitting of data done")

print ("X_train", X_train.shape)
print ("X_test", X_test.shape)

print ("Y_train", Y_train.shape)
print ("Y_test", Y_test.shape)

#########################################################################################
# Step-5: Scale the feature
#########################################################################################

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

print (br)

#########################################################################################
# Step-6.1 Create the Individual Model
#########################################################################################

model_log = LogisticRegression(max_iter=1000)
model_tree = DecisionTreeClassifier(random_state=42)
model_KNN = KNeighborsClassifier(n_neighbors=5)

print ("Individual models created")
print (br)

#########################################################################################
# Step - 6.2 Create the Voting model
########################################################################################

model = VotingClassifier(
    estimators= [
        ('logistic',model_log),
        ('decision_tree', model_tree),
        ('knn',model_KNN)
         ],
    voting= 'hard'
)

print (br)

#######################################################################################
# Step 7.1 Train the Logistic Regression Model
#######################################################################################

model = model.fit (X_train, Y_train)

#########################################################################################
# Step 7.2 Test the Logistic Regression Model
########################################################################################

Y_pred = model.predict(X_test)

########################################################################################
# Step 8 Evaluate the Decision Tree Model
########################################################################################

print (br)
accuracy = accuracy_score(Y_test,Y_pred)
print ("Accuracy : ", accuracy)
print ("Accuracy in percentage: ",accuracy*100)

print (br)







