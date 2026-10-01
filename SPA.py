import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('student.csv')
print("Complete Dataset:")
print(data)

print("\nFirst 5 students:")
print(data.head())

print("\nDataset information:")
data.info()

print("\nBasic statistics:")
print(data.describe())
#avg marks
data["Average_Marks"] = data[["Math", "Python", "DSA"]].mean(axis=1)
print("\nAverage Marks:")
print(data[["Student", "Average_Marks"]])
#highest scorer
highest_scorer = data.loc[data["Average_Marks"].idxmax()]
print("\nHighest Scorer:")
print(highest_scorer[["Student", "Average_Marks"]])
#lowest scorer
lowest_scorer = data.loc[data["Average_Marks"].idxmin()]
print("\nLowest Scorer:")
print(lowest_scorer[["Student", "Average_Marks"]])
# Statistical Analysis
average = data["Average_Marks"].mean()
median = data["Average_Marks"].median()
mode = data["Average_Marks"].mode()
variance = data["Average_Marks"].var()
standard = data["Average_Marks"].std()
percentile_75 = data["Average_Marks"].quantile(0.75)

#print("\nStatistical Analysis:")
#print("Mean:", average)
#print("Median:", median)
#print("Mode:", mode)
#print("Variance:", variance)
#print("Standard Deviation:", standard)
#print("75th Percentile:", percentile_75)
print("Mean:", round(average, 2))
print("Median:", round(median, 2))

if len(mode)== len(data):
    print("Mode: No unique mode")
else:
    print("Mode:", mode.tolist())

print("Variance:", round(variance, 2))
print("Standard Deviation:", round(standard, 2))
print("75th Percentile:", round(percentile_75, 2))

# Correlation Analysis
study_correlation = data["Study_Hours"].corr(data["Average_Marks"])
attendance_correlation = data["Attendance"].corr(data["Average_Marks"])
assignment_correlation = data["Assignments"].corr(data["Average_Marks"])

print("\nCorrelation Analysis:")
print("Study Hours vs Average Marks:", study_correlation)
print("Attendance vs Average Marks:", attendance_correlation)
print("Assignments vs Average Marks:", assignment_correlation)
# Data Cleaning Check
print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())
# Final Findings

print("\nFinal Findings:")

print("Highest Scorer:", highest_scorer["Student"])
print("Highest Average Marks:", round(highest_scorer["Average_Marks"], 2))

print("Lowest Scorer:", lowest_scorer["Student"])
print("Lowest Average Marks:", round(lowest_scorer["Average_Marks"], 2))

print("Average Study Hours:", round(data["Study_Hours"].mean(), 2))
print("Average Attendance:", round(data["Attendance"].mean(), 2))
print("Average Assignments:", round(data["Assignments"].mean(), 2))
# Visualization: Study Hours vs Average Marks

plt.figure(figsize=(8, 5))

plt.scatter(data["Study_Hours"], data["Average_Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.title("Study Hours vs Average Marks")

plt.grid(True)

plt.savefig("study_hours_vs_marks.png", dpi=300, bbox_inches="tight")

plt.show()
plt.close()
