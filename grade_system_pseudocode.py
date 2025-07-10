# Pseudocode for a simple grade system

START
  INPUT student_score
  IF student_score >= 70 THEN
    grade = "A"
  ELSE IF student_score >= 60 THEN
    grade = "B"
  ELSE IF student_score >= 50 THEN
    grade = "C"
  ELSE IF student_score >= 45 THEN
    grade = "D"
  ELSE IF student_score >= 40 THEN
    grade = "E"
  ELSE
    grade = "F"
  END IF
  OUTPUT "The grade is: " + grade
END