#You are going to write a program that calculates the highest score from a List of scores.

#e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

#Important you are not allowed to use the max or min functions. The output words must match the example. i.e

#The highest score in the class is: x

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for student_test in student_scores:
  if student_test > highest_score:
    highest_score = student_test

print(f'The highest score in the class is: {highest_score}')