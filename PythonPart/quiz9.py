text = """
Hi {},

This is a reminder that you have {} assignments
left to submit before you can graduate. Your current grade is {}
and can increase to {} if you submit all assignments
before the due date.
"""

names = input('Enter names separated by commas: ').title().split(',')
assignments = input('Enter # of missing assignments: ').split(',')
grades = input('Enter grades separated by commas: ').split(',')

# for i in range(len(names)):
#     print(text.format(
#         names[i],
#         assignments[i],
#         grades[i],
#         str(int(grades[i]) + 2 * int(assignments[i])))
#     )

for name, missing, grade in zip(names, assignments, grades):
    print(text.format(name, missing, grade, int(grade) + int(missing)*2))
