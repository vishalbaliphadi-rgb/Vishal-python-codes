import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report

)

Border = "=" *30

###########################################################################
# Step-1: Load the file
###########################################################################

print (Border)
print ("Step-1: Load the dataset")
print (Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print ("Dataset Loaded Successfully")
print ("Initial entries from dataset are: ")
print (df.head())
print ("Last few records from dataset are: ")
print (df.tail())

############################################################################
# Step-2: Data Analysis (EDA)
############################################################################

print (Border)
print ("Step-2: Data Analysis")
print (Border)

print ("Shape of Dataset that is total number of Rows and column: ", df.shape )
print ("Column names: ", list(df.columns))

print ("Missing values per column: ")
print (df.isnull().sum())

print ("Class Distribution (FinalResult)")
print (df["FinalResult"].value_counts())

print ("Statistical Report of Dataset:")
print (df.describe)

# Total number of students in DataSet

print (Border)
print ("Total number of students: ", len(df))
print (Border)

# count and percentage of passed and Failed students

count_pass = df["FinalResult"].value_counts().get(1)
pass_percentage = (count_pass/len(df)) * 100
count_fail = df["FinalResult"].value_counts().get(0)
fail_percent = (count_fail/len(df)) *100


print (Border)
print ("Total number of students Passed: ",count_pass)
print ("Total number of students Failed: ",count_fail)
print ("Pass percentage: ", pass_percentage)
print ("Fail Percentage: ", fail_percent)
print (Border)

# Average study hours, Avg Attendance, Max Prev score, Min sleep hours

print (Border)

Avg_Stud_hrs = df["StudyHours"].mean()
print ("Average Study hours", Avg_Stud_hrs)

avg_attend = df["Attendance"].mean()
print ("Avg of attendance", avg_attend)

Max_prev_Score = df["PreviousScore"].max()
print ("Max prev score: ", Max_prev_Score)

Min_sleep_hour = df["SleepHours"].min()
print ("Min Sleep hours: ", Min_sleep_hour)

print (Border)

# Study hours/Higher attendance and Passing analysis

print(Border)

avg_studyhour_pass = df.groupby("FinalResult").get_group(1)["StudyHours"].mean()
print ("Avg study hours of Passed students: ", avg_studyhour_pass)

avg_studyhour_fail = df.groupby("FinalResult").get_group(0)["StudyHours"].mean()
print ("Avg study hours of Failed students: ", avg_studyhour_fail)

print (Border)

avg_attend_pass = df.groupby("FinalResult").get_group(1)["Attendance"].mean()
print ("Avg attendance of Passed students: ", avg_attend_pass)

avg_attend_fail = df.groupby("FinalResult").get_group(0)["Attendance"].mean()
print ("Avg attendance of Failed students: ", avg_attend_fail)

print (Border)
print ("As per above analysis Higher the study hours it increases chance of passing")
print ("As per above analysis Higher the attendance it increases chances of Passing")
print (Border)

# Plotting Histogram of StudyHours

print (Border)
print ("Plotting Histogram of StudyHours")
print (Border)

df["StudyHours"].hist(bins=5, color = "skyblue", edgecolor = "black")

plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Histogram of Study Hours")
plt.show()

# Scatter Plot for Visualization of Dataset

print (Border)
print ("Scatter Plot for Visualization of Dataset")
print (Border)

plt.figure (figsize= (7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"]==sp]
    plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = sp)

plt.title ("Marvellous Student Performance case study")

plt.xlabel ("StudyHours")
plt.ylabel("PreviousScore")

plt.legend()
plt.grid()
plt.show()

# Boxplot for attendance

print (Border)
print ("BoxPlot for attendance")
print (Border)

df.boxplot(column = ["Attendance"])

# Create a plot showing relationship between assignments Completed and Final result

print (Border)
print ("Plot showing relationship between assignments completed and Final Result")
print (Border)

plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"]==sp]
    plt.scatter(temp["AssignmentsCompleted"], temp["FinalResult"], label = sp)

plt.title ("Marvellous Student Performance")

plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")

plt.legend()
plt.grid()
plt.show()

print ("More the Assignment Completed more the passing chances")

# Create a plot showing relationship between Sleep hours and Final result

print (Border)
print ("Plot showing Relationship between Sleep hours and Final Result")
print (Border)

plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"]==sp]
    plt.scatter(temp["SleepHours"], temp["FinalResult"], label =sp)

plt.title("Marvellous Student Performance plot")

plt.xlabel("SleepHours")
plt.ylabel("FinalResult")

plt.legend()
# plt.grid()
plt.show()

print ("Students with more sleep hours showing good passing chances")



