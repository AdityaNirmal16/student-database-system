import sqlite3

# ==============================
# DATABASE SETUP
# ==============================
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
conn.commit()


# ==============================
# FUNCTIONS
# ==============================

# Add Student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    print("✅ Student added!\n")


# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n--- Students ---")
    if not rows:
        print("No records found.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    print()


# Update Student
def update_student():
    student_id = int(input("Enter ID to update: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    if not cursor.fetchone():
        print("❌ Student not found!\n")
        return

    name = input("New name: ")
    age = int(input("New age: "))
    course = input("New course: ")

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, student_id)
    )
    conn.commit()
    print("✅ Student updated!\n")


# Delete Student
def delete_student():
    student_id = int(input("Enter ID to delete: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    if not cursor.fetchone():
        print("❌ Student not found!\n")
        return

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("✅ Student deleted!\n")


# ==============================
# MENU SYSTEM
# ==============================

def menu():
    while True:
        print("===== Student Database Menu =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.\n")


# ==============================
# RUN PROGRAM
# ==============================
menu()

# Close connection when program ends
conn.close()