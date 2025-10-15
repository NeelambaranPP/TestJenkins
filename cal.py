students = []
def add_student(name, regno):
    student = {"name": name, "regno": regno}
    students.append(student)
    return student
def get_all_students():
    return students
if __name__ == "__main__":
    add_student("Neel", "SSN001")
    add_student("kapil", "SSN002")
    print("Student List:")

    for s in get_all_students():
        print(f"Name: {s['name']} | RegNo: {s['regno']}")
