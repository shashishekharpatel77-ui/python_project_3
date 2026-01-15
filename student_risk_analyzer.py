"""
======================================================================
PROJECT : Student Performance Progression & Risk Analyzer (Major Project)
AUTHOR  : Shashi Shekhar Patel (CSE 3rd Sem)
NOTE    : This project analyzes student academic data to identify 
          'At-Risk' students, subject difficulty, and progression trends.
======================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- STEP 1: LOAD DATA ---
print(">>> Step 1: Loading Dataset...")

file_name = 'StudentsPerformance.csv'

if os.path.exists(file_name):
    df = pd.read_csv(file_name)
    print(f"Success: '{file_name}' loaded. Total Students: {len(df)}")
else:
    print(f"Error: '{file_name}' not found. Please put the CSV in this folder.")
    exit()

# Add Student ID
df.insert(0, 'Student_ID', [f'STD_{i+1001}' for i in range(len(df))])

# Calculate Average Score
df['Average_Score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3


# --- STEP 2: DATA ENGINEERING & LOGIC ---
print(">>> Step 2: Processing Logic & Risk Analysis...")
np.random.seed(42)

# 1. Simulated Attendance
df['Attendance_Pct'] = df['Average_Score'].apply(
    lambda x: min(100, max(45, int(x + np.random.randint(-15, 10))))
)

# 2. Semester Progression
df['Sem1_Score'] = df['Average_Score'].apply(
    lambda x: min(100, max(0, int(x + np.random.randint(-12, 12))))
)
df['Sem2_Score'] = df['Average_Score']

# 3. Consistency Score (Standard Deviation)
df['Consistency_Score'] = df[['Sem1_Score', 'Sem2_Score']].std(axis=1).round(2)

# 4. Risk Status (Rule-Based)
df['Risk_Status'] = np.where(
    (df['Attendance_Pct'] < 75) | (df['Average_Score'] < 40), 
    'High Risk', 
    'Safe'
)

# 5. NEW: Risk Score (0–100) → Advanced Feature
df['Risk_Score'] = (
    (100 - df['Attendance_Pct']) * 0.4 +
    (100 - df['Average_Score']) * 0.6
).round(2)


# --- STEP 3: VISUALIZATION ---
print(">>> Step 3: Generating Analytical Graphs...")
sns.set_style("whitegrid")

# GRAPH 1: Correlation Heatmap
plt.figure(figsize=(10, 6))
correlation_data = df[['Attendance_Pct', 'Sem1_Score', 'Sem2_Score', 'math score']].corr()
sns.heatmap(correlation_data, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Analysis: Impact of Attendance on Marks')
plt.savefig('MAJOR_Graph_1_Correlation.png', dpi=200)
plt.close()

# GRAPH 2: Risk Distribution (Donut Chart)
plt.figure(figsize=(6, 6))
risk_counts = df['Risk_Status'].value_counts()
plt.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', 
        colors=['#2ecc71', '#e74c3c'], startangle=90, wedgeprops={'width':0.4})
plt.title('Student Dropout Risk Analysis (Safe vs High Risk)')
plt.savefig('MAJOR_Graph_2_Risk_Chart.png', dpi=200)
plt.close()

# GRAPH 3: Performance Trend (Top 5 At-Risk Students)
plt.figure(figsize=(10, 5))
sample_risk = df[df['Risk_Status'] == 'High Risk'].head(5)

for i, row in sample_risk.iterrows():
    plt.plot(['Sem 1', 'Sem 2'], [row['Sem1_Score'], row['Sem2_Score']], 
             marker='o', linestyle='--', label=row['Student_ID'])

plt.axhline(y=40, color='red', linestyle='-', linewidth=2, alpha=0.5)
plt.text(0.5, 42, 'Passing Threshold (40 Marks)', color='red', fontsize=10)

plt.title('Performance Progression of At-Risk Students')
plt.ylabel('Score (0-100)')
plt.legend()
plt.savefig('MAJOR_Graph_3_Trend_Analysis.png', dpi=200)
plt.close()

# GRAPH 4: Subject Difficulty Analysis (Box Plot)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['math score', 'reading score', 'writing score']], palette="Set2")
plt.title('Subject Difficulty Analysis (Score Distribution)')
plt.savefig('MAJOR_Graph_4_Subject_Difficulty.png', dpi=200)
plt.close()

# GRAPH 5: NEW – Risk Score Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Risk_Score'], bins=20, kde=True)
plt.title("Risk Score Distribution of Students")
plt.xlabel("Risk Score (0 = Safe, 100 = Extreme Risk)")
plt.savefig("MAJOR_Graph_5_Risk_Score_Distribution.png", dpi=200)
plt.close()


# --- STEP 4: FINAL REPORT ---
subject_means = df[['math score', 'reading score', 'writing score']].mean()
toughest_subject = subject_means.idxmin()

top_risk = df.sort_values(by='Risk_Score', ascending=False).head(10)

print("\n" + "="*60)
print("   MAJOR PROJECT REPORT: Student Performance & Risk Analyzer")
print("="*60)
print(f" Total Students Analyzed : {len(df)}")
print(f" High Risk Students      : {len(df[df['Risk_Status'] == 'High Risk'])}")
print(f" Toughest Subject        : {toughest_subject.title()} (Avg: {subject_means.min():.1f})")
print("-" * 60)
print(" Top 10 At-Risk Students:")
print(top_risk[['Student_ID','Attendance_Pct','Average_Score','Risk_Score']])
print("-" * 60)
print(" Success! 5 Graphs Generated:")
print(" 1. MAJOR_Graph_1_Correlation.png")
print(" 2. MAJOR_Graph_2_Risk_Chart.png")
print(" 3. MAJOR_Graph_3_Trend_Analysis.png")
print(" 4. MAJOR_Graph_4_Subject_Difficulty.png")
print(" 5. MAJOR_Graph_5_Risk_Score_Distribution.png")
print("="*60 + "\n")
