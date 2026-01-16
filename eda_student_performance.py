import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create folder for visualizations
os.makedirs("visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv("student_performance_dataset.csv")

# Basic information
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# =========================
# Study Hours Distribution
# =========================
study_hours_counts = df["Study_Hours_Per_Week"].value_counts().sort_index()

plt.figure()
plt.bar(study_hours_counts.index, study_hours_counts.values)
plt.xlabel("Study Hours Per Week")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours (Bar Chart)")
plt.savefig("visualizations/study_hours_bar_chart.png")
plt.show()

# =================
# Math Score Boxplot
# =================
plt.figure()
sns.boxplot(x=df["Math_Score"])
plt.title("Math Score Distribution")
plt.savefig("visualizations/math_score_boxplot.png")
plt.show()

# ============================
# Study Hours vs Math Score
# ============================
plt.figure()
plt.scatter(df["Study_Hours_Per_Week"], df["Math_Score"])
plt.xlabel("Study Hours Per Week")
plt.ylabel("Math Score")
plt.title("Study Hours vs Math Score")
plt.savefig("visualizations/study_hours_vs_math_score.png")
plt.show()

# ==============================
# Attendance vs Science Score
# ==============================
plt.figure()
plt.scatter(df["Attendance_Percentage"], df["Science_Score"])
plt.xlabel("Attendance Percentage")
plt.ylabel("Science Score")
plt.title("Attendance vs Science Score")
plt.savefig("visualizations/attendance_vs_science_score.png")
plt.show()

# =================
# Correlation Heatmap
# =================
plt.figure(figsize=(8, 6))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True
)
plt.title("Correlation Heatmap")
plt.savefig("visualizations/correlation_heatmap.png")
plt.show()
