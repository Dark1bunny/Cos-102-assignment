#Grade System

score = float(input("Enter your score: "))
# Determine the grade based on the score
if 70 <= score <= 100:
    grade = "A"
elif 60 <= score < 70:
    grade = "B"
elif 50 <= score < 60:
    grade = "C"
elif 45 <= score < 50:
    grade = "D"
elif 40 <= score < 45:
    grade = "E"
elif 0 <= score < 40:
    grade = "F"
else:
    grade = "Invalid score"

print(f"Your grade is: {grade}")