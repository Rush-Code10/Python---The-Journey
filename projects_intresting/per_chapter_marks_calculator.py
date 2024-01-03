subject = input("Enter subject: ")
total_marks = int(input("Enter total number of marks: "))
unit_name = input("Enter chapter name: ")
time_unit = int(input("Enter time taken for the unit: "))
time_sub = int(input("Enter total time allocated to the subject: "))

marks = float(time_unit/time_sub)*total_marks

print(f"{unit_name} has around {marks} allocated out of {total_marks}")