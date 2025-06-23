student = {
    "name": "Alice",
    "age": 20,
    "grade level": "2nd year",
    "courses": {
        "Math": "10", 
        "History": "9", 
        "Lithuanian": "8"}
}
# Print initial student information
print("Initial student record:")
for key, value in student.items():
    print(f"{key}: {value}")

# Add a new course and grade
new_course = input("\nEnter the name of a new course to add: ")
new_grade = input(f"Enter the grade for {new_course}: ")

# Update the dictionary
student["courses"][new_course] = new_grade

# Print updated student record
print("\nUpdated student record:")
for key, value in student.items():
    print(f"{key}: {value}")