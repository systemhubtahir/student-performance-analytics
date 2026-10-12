# Project Documentation

## 1. Project Title
**Student Performance Analytics System**

- Student name: Md shaik tahir hussain
- AICTE Student ID: STU90a57f5a2045c1790012302
- Application: INTERNSHIP_17900042406ab14c1037b3c
- Course: Python with AI 

## 2. Objective
Teachers often hold student marks in a plain table and must work out totals, grades and pass/fail results by hand. This is slow and easy to get wrong. This project reads student records from a CSV file and does the calculations automatically. It reports each student's total, average, grade and result. It also shows subject-wise performance, the top performers and attendance. The output is clear enough to read without opening the code.

## 3. Technologies Used
- **Python 3** for the program logic, functions, loops and conditions
- **Pandas** for loading the CSV, storing data in a DataFrame, sorting, filtering and column calculations
- **NumPy** for numerical calculations (total marks and average attendance)
- **Git and GitHub** for version control and publishing

## 4. Dataset Description
The file `students.csv` holds 20 fictional student records. It has no missing values and every Student ID is unique.

| Column | Description |
|---|---|
| StudentID | Unique ID of the student (101 to 120) |
| Name | Student name |
| Department | Computer Science, Mathematics or Physics |
| Maths, Science, English, Computer | Subject marks out of 100 |
| Attendance | Attendance percentage |

## 5. Implementation
1. **Load data.** `pd.read_csv("students.csv")` reads the file into a DataFrame.
2. **Inspect data.** The program prints the first five rows with `head()`, the size with `shape`, the column names, and `info()`.
3. **Total marks.** `calculate_total()` converts the four subject columns to a NumPy array and sums each row with `np.sum(..., axis=1)`.
4. **Average marks.** `calculate_average()` uses Pandas `mean(axis=1)` and rounds to two decimals.
5. **Grades.** `assign_grade()` uses if/elif conditions on the average and is applied to every row with `apply()`.
6. **Pass/fail.** `pass_fail()` loops over the four subjects. A student fails if any subject mark is below 40.
7. **Top performers.** `top_performers()` sorts by average in descending order and returns the first 3 rows.
8. **Subject analysis.** `subject_analysis()` loops over the subjects and prints the mean, highest and lowest marks of each.
9. **Attendance analysis.** `attendance_analysis()` uses NumPy to find average attendance. It filters students below 75% with a Pandas condition.
10. **Answer the project questions.** The program finds the highest-average student with `idxmax()`, the best subject, the pass and fail counts, and the class average.
11. **Save results.** `df.to_csv("student_results.csv")` saves the full analysed table.

**Grading rule**

| Average | Grade |
|---|---|
| 90 and above | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 40 to below 60 | D |
| Below 40 | F |

**Pass condition:** a student passes only if every subject mark is at least 40.

## 6. Key Features
- Dataset loading and inspection with Pandas
- Reusable functions: `calculate_total`, `calculate_average`, `assign_grade`, `pass_fail`, `top_performers`, `subject_analysis`, `attendance_analysis`
- Total and average marks per student
- Grade assignment with a clear rule
- Pass/fail rule applied to every subject
- Top 3 students list
- Subject-wise mean, highest and lowest marks
- Attendance summary and low-attendance list
- Answers to the four project questions
- Results saved to `student_results.csv`

## 7. Output
Output of `python main.py`:

```text
STUDENT PERFORMANCE ANALYTICS
=======================================================

First five records:
 StudentID   Name       Department  Maths  Science  English  Computer  Attendance
       101  Aarav Computer Science     92       88       85        96          95
       102   Diya Computer Science     85       91       89        94          92
       103  Rohan      Mathematics     78       82       75        80          88
       104 Ananya Computer Science     95       93       90        98          97
       105 Vikram      Mathematics     45       52       48        55          72

Dataset shape: (20, 8)

Column names: ['StudentID', 'Name', 'Department', 'Maths', 'Science', 'English', 'Computer', 'Attendance']

Dataset information:
<class 'pandas.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   StudentID   20 non-null     int64
 1   Name        20 non-null     str  
 2   Department  20 non-null     str  
 3   Maths       20 non-null     int64
 4   Science     20 non-null     int64
 5   English     20 non-null     int64
 6   Computer    20 non-null     int64
 7   Attendance  20 non-null     int64
dtypes: int64(6), str(2)
memory usage: 1.4 KB

STUDENT RESULTS
=====================================================================================
 StudentID   Name  Total  Average Grade Result
       101  Aarav    361    90.25     A   Pass
       102   Diya    359    89.75     B   Pass
       103  Rohan    315    78.75     B   Pass
       104 Ananya    376    94.00     A   Pass
       105 Vikram    200    50.00     D   Pass
       106  Meera    350    87.50     B   Pass
       107  Arjun    192    48.00     D   Fail
       108   Isha    319    79.75     B   Pass
       109  Kabir    253    63.25     C   Pass
       110  Sneha    387    96.75     A   Pass
       111  Rahul    169    42.25     D   Fail
       112  Priya    332    83.00     B   Pass
       113 Aditya    235    58.75     D   Pass
       114  Kavya    360    90.00     A   Pass
       115  Manoj    141    35.25     F   Fail
       116   Neha    317    79.25     B   Pass
       117  Imran    272    68.00     C   Pass
       118  Pooja    347    86.75     B   Pass
       119  Karan    163    40.75     D   Fail
       120  Farah    316    79.00     B   Pass

TOP 3 PERFORMERS
-------------------------------------------------------
  Name       Department  Average Grade
 Sneha Computer Science    96.75     A
Ananya Computer Science    94.00     A
 Aarav Computer Science    90.25     A

SUBJECT-WISE ANALYSIS
-------------------------------------------------------
Maths      Mean: 69.70 | Highest: 98 | Lowest: 28
Science    Mean: 70.40 | Highest: 96 | Lowest: 33
English    Mean: 72.00 | Highest: 94 | Lowest: 35
Computer   Mean: 76.10 | Highest: 99 | Lowest: 42

ATTENDANCE ANALYSIS
-------------------------------------------------------
Average attendance: 83.40%
Students below 75% attendance: 5
  Vikram   72%  (Pass)
  Arjun    68%  (Fail)
  Rahul    60%  (Fail)
  Manoj    55%  (Fail)
  Karan    65%  (Fail)

PROJECT QUESTIONS: ANSWERS
=======================================================
1. Highest average: Sneha (96.75)
2. Best subject by class mean: Computer (76.10)
3. Students passed: 16 out of 20
   Students failed: 4 out of 20
4. Class average: 72.05

Results saved to student_results.csv
```

## 8. Final Outcome
The program runs without errors and gives these results for the 20-student dataset:
- Highest average: **Sneha (96.75, grade A)**
- Top three: Sneha (96.75), Ananya (94.00), Aarav (90.25)
- Best subject by class mean: **Computer (76.10)**
- Passed: **16 of 20**. Failed: 4 of 20 (Arjun, Rahul, Manoj, Karan)
- Class average: **72.05**
- Average attendance: 83.40%. Four of the five students below 75% attendance also failed.

The project meets the brief. It uses Pandas, NumPy, functions and loops, and it produces readable results.

## 9. Challenges & Learning
- **Pass rule.** Average alone was not enough. Arjun (average 48.00) and Rahul (average 42.25) have averages above 40 but fail because one subject is below 40. I solved this with a loop in `pass_fail()` that checks every subject.
- **Grade and result are separate.** A student can have grade D and still fail. I kept the grade rule and the pass rule as two functions.
- **Order of steps.** The grade needs the average, and the average needs the marks. I learned to call the functions in the right order.
- **NumPy and Pandas together.** I used NumPy for numerical work and Pandas for loading, sorting and filtering. I learned where each one is the better tool.
- **Running the program.** The script reads `students.csv` by relative path, so it must run from inside the project folder.

<!-- Replace or add problems you personally faced. -->

## 10. GitHub Repository
https://github.com/systemhubtahir/student-performance-analytics.git
