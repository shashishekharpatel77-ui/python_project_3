# Student Performance & Risk Analyzer

### Project Description
This is my Major Project where I analyzed student exam data to understand their performance. The main goal of this project is to identify students who are "At Risk" (likely to fail) based on their marks in Math, Reading, and Writing.

This analysis helps in finding out which students need more attention to improve their results.

### How it Works
I used a dataset (`StudentsPerformance.csv`) that contains marks and other details like parental education level and test preparation.

The Python script does the following steps:
1.  **Loads Data:** It reads the data from the CSV file using Pandas.
2.  **Analyzes Scores:** It checks the marks of students in different subjects.
3.  **Risk Assessment:** It adds a logic to classify students into "Pass" or "High Risk" based on a cutoff score.

### Files in this Repository
* `student_risk_analyzer.py`: The main Python code for the project.
* `StudentsPerformance.csv`: The dataset file containing the students' marks.

### How to Run
1.  Download both the `.py` code file and the `.csv` dataset.
2.  Keep both files in the **same folder**.
3.  Make sure you have Python installed with the necessary libraries (pandas, matplotlib, seaborn).
4.  Run the script to see the analysis.
