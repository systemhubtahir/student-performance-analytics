# Student Performance Analytics

## Title
**Student Performance Analytics  System**

Student: **Md shaik tahir hussain** | AICTE Student ID: **STU90a57f5a2045c1790012302** | Application: **INTERNSHIP_17900042406ab14c1037b3c**

## Objective
Analyse student marks and attendance with Python. Calculate totals, averages, grades and pass/fail status. Find top performers and subject-wise performance.

## Technologies Used
- Python 3
- Pandas
- NumPy
- Git and GitHub (for version control and publishing)

## Dataset
The file `students.csv` contains 20 sample student records. Columns include:
- `StudentID`: unique student identifier
- `Name`: student name
- `Department`: academic department
- `Maths`, `Science`, `English`, `Computer`: marks from 0 to 100
- `Attendance`: attendance percentage

The data is fictional and intended for educational demonstration.

##  Key Features
- Dataset inspection
- Total and average calculation
- Grade assignment
- Subject-wise pass/fail evaluation
- Top-three performer listing
- Subject-level statistics
- Attendance analysis (average and low-attendance students)
- Export of analysed results

### Grade rules
| Average | Grade |
|---|---|
| 90 and above | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 40 to below 60 | D |
| Below 40 | F |

A student can have an average above 40 and still fail if any one subject is below 40.

## Outcome
Running `python main.py` on the 20-record dataset gives:
- Highest average: Sneha (96.75, grade A)
- Top three: Sneha, Ananya (94.00), Aarav (90.25)
- Best subject by class mean: Computer (76.10)
- Passed: 16 of 20. Failed: 4 of 20 (Arjun, Rahul, Manoj, Karan)
- Class average: 72.05

The program prints every result in the terminal and saves the full table to `student_results.csv`.

---

## How to Run

1. Install Python 3.
2. Open a terminal in this project folder.
3. Install dependencies:

   ```bash
   python -m pip install pandas numpy
   ```

4. Run the program:

   ```bash
   python main.py
   ```

The program creates `student_results.csv` in the same folder.
