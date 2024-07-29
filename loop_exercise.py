student_scores = input("Enter the student scores").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
print (student_scores)

highest_student_score = 0

for score in student_scores:
    if score > highest_student_score:
        highest_student_score = score
print (highest_student_score)