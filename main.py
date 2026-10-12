import pandas as pd
import numpy as np

# Subject columns used for analysis
SUBJECTS = ["Maths", "Science", "English", "Computer"]


def calculate_total(df):
    """Calculate total marks for each student using NumPy."""
    df["Total"] = np.sum(df[SUBJECTS].to_numpy(), axis=1)
    return df


def calculate_average(df):
    """Calculate average marks for each student."""
    df["Average"] = df[SUBJECTS].mean(axis=1).round(2)
    return df


def assign_grade(avg):
    """Assign a grade based on the student's average."""
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def pass_fail(row):
    """Pass only if every subject mark is at least 40."""
    for subject in SUBJECTS:
        if row[subject] < 40:
            return "Fail"
    return "Pass"


def top_performers(df, n=3):
    """Return the top n students by average marks."""
    return df.sort_values(by="Average", ascending=False).head(n)


def subject_analysis(df):
    """Display mean, maximum, and minimum for each subject."""
    print("\nSUBJECT-WISE ANALYSIS")
    print("-" * 55)

    for subject in SUBJECTS:
        mean_marks = df[subject].mean()
        max_marks = df[subject].max()
        min_marks = df[subject].min()

        print(
            f"{subject:<10} "
            f"Mean: {mean_marks:.2f} | "
            f"Highest: {max_marks} | "
            f"Lowest: {min_marks}"
        )


def attendance_analysis(df, threshold=75):
    """Display average attendance and students below the threshold."""
    print("\nATTENDANCE ANALYSIS")
    print("-" * 55)

    average_attendance = np.mean(df["Attendance"].to_numpy())
    low_attendance = df[df["Attendance"] < threshold]

    print(f"Average attendance: {average_attendance:.2f}%")
    print(f"Students below {threshold}% attendance: {len(low_attendance)}")
    for _, student in low_attendance.iterrows():
        print(f"  {student['Name']:<8} {student['Attendance']}%  ({student['Result']})")


def main():
    # Load the dataset from the same folder as this script
    df = pd.read_csv("students.csv")

    # Inspect the dataset
    print("STUDENT PERFORMANCE ANALYTICS")
    print("=" * 55)

    print("\nFirst five records:")
    print(df.head().to_string(index=False))

    print("\nDataset shape:", df.shape)
    print("\nColumn names:", df.columns.tolist())

    print("\nDataset information:")
    df.info()

    # Calculate student performance
    calculate_total(df)
    calculate_average(df)
    df["Grade"] = df["Average"].apply(assign_grade)
    df["Result"] = df.apply(pass_fail, axis=1)

    # Display student results
    print("\nSTUDENT RESULTS")
    print("=" * 85)
    print(
        df[["StudentID", "Name", "Total", "Average", "Grade", "Result"]]
        .to_string(index=False)
    )

    # Display top three performers
    print("\nTOP 3 PERFORMERS")
    print("-" * 55)
    print(
        top_performers(df, 3)[["Name", "Department", "Average", "Grade"]]
        .to_string(index=False)
    )

    # Analyse each subject
    subject_analysis(df)

    # Analyse attendance
    attendance_analysis(df)

    # Answer the four project questions
    highest = df.loc[df["Average"].idxmax()]
    best_subject = df[SUBJECTS].mean().idxmax()
    pass_count = (df["Result"] == "Pass").sum()
    fail_count = (df["Result"] == "Fail").sum()
    class_average = df["Average"].mean()

    print("\nPROJECT QUESTIONS: ANSWERS")
    print("=" * 55)
    print(f"1. Highest average: {highest['Name']} ({highest['Average']:.2f})")
    print(
        f"2. Best subject by class mean: {best_subject} "
        f"({df[best_subject].mean():.2f})"
    )
    print(f"3. Students passed: {pass_count} out of {len(df)}")
    print(f"   Students failed: {fail_count} out of {len(df)}")
    print(f"4. Class average: {class_average:.2f}")

    # Save the analysed results for future reference
    df.to_csv("student_results.csv", index=False)
    print("\nResults saved to student_results.csv")


if __name__ == "__main__":
    main()
