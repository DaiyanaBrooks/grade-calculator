# Grade Calculator Program

This project is a **Grade Calculator** program written in Python. It helps users calculate and display a student's final grade based on their grades in various categories (e.g., Homework, Program Assignments, Quizzes, Tests, Final Exam). The program allows the user to input grades for each category and computes the weighted total to determine the final letter grade.

## Features
- **Grade Input**: Users can input grades for different categories such as Homework, Program Assignments, Quizzes, Tests, and Final Exam.
- **Weighted Calculation**: The program calculates the weighted total for each category based on predefined weights.
- **Final Grade Calculation**: It calculates the overall grade based on the weighted totals and outputs the corresponding letter grade.
- **Flexible Input**: Grades can be entered multiple times for categories like Homework and Program Assignments, but only once for the Final Exam.

## Categories and Weights
The program uses the following categories with corresponding weights to calculate the final grade:
- **Homework**: 10%
- **Program Assignments**: 30%
- **Quiz**: 15%
- **Test**: 20%
- **Final Exam**: 25%

## How to Use
1. **Run the program**:
   - Download the Python file (`grade_calculator.py`).
   - Open your terminal or command prompt.
   - Navigate to the folder where the file is saved.
   - Run the program with the command:
     ```bash
     python grade_calculator.py
     ```
2. **Input your grades**:
   - The program will prompt you to enter grades for each category.
   - Enter each grade and press **Enter**.
   - To stop entering grades for a category (other than the Final Exam), type `-1` and press **Enter**.

3. **Get your result**:
   - After entering all grades, the program will display the weighted totals for each category and your final grade, along with the corresponding letter grade.

## Example
Here’s an example of how the program might look during execution:

```plaintext
Homework category
Enter grade for category Homework : 85
Enter grade for category Homework : 90
Enter grade for category Homework : -1
Program Assignments category
Enter grade for category Program Assignments : 95
Enter grade for category Program Assignments : 88
Enter grade for category Program Assignments : -1
Quiz category
Enter grade for category Quiz : 80
Test category
Enter grade for category Test : 92
Final Exam category
Enter grade for category Final Exam : 85

Homework weighted total is 8.75
Program Assignments weighted total is 26.55
Quiz weighted total is 12.00
Test weighted total is 18.40
Final Exam weighted total is 21.25

Your weighted total in the class is : 86.95
Your letter grade in the class is B+
```
## Requirements
- Python 3.x or later
