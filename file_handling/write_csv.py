import csv

with open('student.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Enl", "Name", "Branch"])
    writer.writerow([201, "Ankit", "CSE"])
    writer.writerow([202, "Aman", "CSE"])
    