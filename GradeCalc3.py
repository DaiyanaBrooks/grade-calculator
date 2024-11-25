""" Daiyana Brooks
October 10th, 2023
Description: This program creates a program that calculates and displays a student's final grade in multiple classes
based on their grades in different categories. The program allows the user to input grades for each category.
"""
#Created a dictionary for categories (Ex: Homework, Quiz, etc) and weights for Comp163Cat and Comp163CatGrades
comp163Cat = {"Homework": .10, "Program Assignments": .30, "Quiz": .15, "Test": .20, "Final Exam": .25}
comp163CatGrades = {"Homework": 0, "Program Assignments": 0, "Quiz": 0, "Test": 0, "Final Exam": 0}

#Goes through the categories and calculates the category grade weighted totals
for category, weights in comp163Cat.items():
    catGrade = [] #makes a list to store category grades
    print(f"{category} category")
    if category != "Final Exam":
        while True:
            grades = float(input(f"Enter grade for category {category} : "))
            if grades == -1:
                break
            catGrade.append(grades)
    else:
        grades = float(input(f"Enter grade for category {category} : "))
        catGrade.append(grades)
    average = sum(catGrade) / len(catGrade)
    comp163CatGrades[category] = average * comp163Cat[category]
#Makes the program print a weighted total per category
for category in comp163CatGrades:
    print(f"{category} weighted total is {comp163CatGrades[category]:.2f}")

#a variable called total_grade is assigned to the sum of comp163CatGrades values.
total_grade = sum(comp163CatGrades.values())
#the code uses If statements to display a letter based on the inputted value from the user.
if total_grade >= 90:
    letter_grade = "A"
if total_grade < 90:
    letter_grade = "A-"
if total_grade < 85:
    letter_grade = "B+"
if total_grade < 82:
    letter_grade = "B"
if total_grade < 78:
    letter_grade = "B-"
if total_grade < 75:
    letter_grade = "C+"
if total_grade < 72:
    letter_grade = "C"
if total_grade < 68:
    letter_grade = "C-"
if total_grade < 65:
    letter_grade = "D+"
if total_grade < 60:
    letter_grade = "D"
if total_grade < 55:
    letter_grade = "F"
#print statements that pull total_grade and letter_grade.
print(f"Your weighted total in the class is : {total_grade:.2f}")
print(f"Your letter grade in the class is {letter_grade}")
