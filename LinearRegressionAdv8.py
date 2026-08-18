import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousRegression(DataPath):
    
    # Step1: Load the data

    br = "-"*40

    print (br)
    print ("Step1: Load the data")
    print (br)

    df = pd.read_csv(DataPath)

    print (df.head())

    # Step2: Remove Unwanted columns

    print (br)
    print ("Step2: Remove unwanted columns")
    print (br)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print (df.head())


    # Step3: Check missing values

    print (br)
    print ("Step3: Check missing values")
    print (br)

    print ("Missing values:" )
    print (df.isnull().sum())


    # Step4: Statistical Summary

    print (br)
    print ("Step4: Statisctical summary")
    print (br)

    print (df.describe())

    # Step5 :Correlation

    print (br)
    print ("Correlation")
    print (br)

    print (df.corr())

    # Step6: Seperate Independent and Dependent variable

    print (br)
    print ("Seperate Independent and Dependent variable")
    print (br)

    X = df[["TV","radio", "newspaper"]]
    Y = df["sales"]

    print ("Independent Variables: ", X.head())
    print ("Dependent Variables: ", Y.head())

    # Step7: Split independent and dependent

    X_train, X_test, Y_train, Y_test = train_test_split(

        X,
        Y,
        test_size= 0.2,
        random_state= 42
    )

    print ("Training Data: ", X_train.shape)
    print ("Testing Data: ", X_test.shape)


    # Step8: Create and Train the model

    print (br)
    print ("Create and Train the model")
    print (br)

    model = LinearRegression()

    model = model.fit (X_train, Y_train)
    print ("Model Trained Succesfully")

    # Step9: Test the Model 

    print (br)
    print ("Test the Model")
    print (br)

    Y_pred = model.predict(X_test)

    print ("expected answers: ")
    print (Y_test[:3])

    print ("Predicted Answers: ")
    print (Y_pred [:3])

    print (Y_pred[:5])

    # Step10: Evaluate the model

    print (br)
    print ("Evaluate the model")
    print (br)

    MSE = mean_squared_error (Y_test, Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score (Y_test, Y_pred)

    print ("MSE: mean square error", MSE)
    print ("Root mean square error: ", RMSE)
    print ("R square: ", R2)

    # Step 11 : Display Coefficient 

    print (br)
    print ("Display Coefficient")
    print (br)

    print ("TV coefficient: ", model.coef_[0])
    print ("Radio coefficient: ", model.coef_[1])
    print ("newspaper coefficient: ", model.coef_[2])

    print ("Intercept: ", model.intercept_)   



def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()