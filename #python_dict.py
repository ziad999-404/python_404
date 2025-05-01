#python_dict
print("first_task :")
contacts = {}
contacts["mohamed"] = "123-456-7890"
contacts["ahmed"] = "987-654-3210"
contacts["mahmoud"] = "555-666-7777"

print("Contact Names:")
for name in contacts:
    print(name)

search_name = input()

if search_name in contacts:
    print(f"{search_name}'s phone number is {contacts[search_name]}")
else:
    print("Contact not found.")

# second_task :     
print("second_task :")       
students = [
    {"name": "ahmed", "grades": [85, 90, 78]},
    {"name": "mohamed", "grades": [72, 88, 91]},
    {"name": "mahmoud", "grades": [95, 87, 93]}
]

for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{name}'s average grade is {average:.2f}")