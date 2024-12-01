subject_1 = int(input("Enter the marks of subject 1: "))

subject_2 = int(input("Enter the marks of subject 2: "))

subject_3 = int(input("Enter the marks of subject 3: "))

subject_4 = int(input("Enter the marks of subject 4: "))

subject_5 = int(input("Enter the marks of subject 5: "))

Aggregate_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5

Percentage = (Aggregate_marks/500) * 100

print(f"Aggregate marks of student: {Aggregate_marks}")

print(f"Percentage of student: {Percentage}%")