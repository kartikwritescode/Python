from pathlib import Path

# Get the Django project root
# create.py is located at:
# student_project/students/templates/students/create.py
project_root = Path(__file__).resolve().parents[3]

# Correct Django template directory
template_dir = project_root / "students" / "templates" / "students"

template_dir.mkdir(parents=True, exist_ok=True)

templates = {
    "student_list.html": """<!DOCTYPE html>
<html>
<head>
    <title>Student List</title>
</head>
<body>

<h1>Student List</h1>

<a href="{% url 'student_create' %}">
    Add New Student
</a>

<br><br>

<table border="1" cellpadding="10">

    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Roll No</th>
        <th>Email</th>
        <th>Course</th>
        <th>Age</th>
        <th>Actions</th>
    </tr>

    {% for student in students %}

    <tr>
        <td>{{ student.id }}</td>
        <td>{{ student.name }}</td>
        <td>{{ student.roll_no }}</td>
        <td>{{ student.email }}</td>
        <td>{{ student.course }}</td>
        <td>{{ student.age }}</td>

        <td>
            <a href="{% url 'student_detail' student.id %}">
                View
            </a>

            |

            <a href="{% url 'student_update' student.id %}">
                Edit
            </a>

            |

            <a href="{% url 'student_delete' student.id %}">
                Delete
            </a>
        </td>
    </tr>

    {% empty %}

    <tr>
        <td colspan="7">
            No students available.
        </td>
    </tr>

    {% endfor %}

</table>

</body>
</html>
""",

    "student_detail.html": """<!DOCTYPE html>
<html>
<head>
    <title>Student Details</title>
</head>
<body>

<h1>Student Details</h1>

<p><strong>ID:</strong> {{ student.id }}</p>
<p><strong>Name:</strong> {{ student.name }}</p>
<p><strong>Roll No:</strong> {{ student.roll_no }}</p>
<p><strong>Email:</strong> {{ student.email }}</p>
<p><strong>Course:</strong> {{ student.course }}</p>
<p><strong>Age:</strong> {{ student.age }}</p>

<br>

<a href="{% url 'student_list' %}">
    Back to Student List
</a>

|

<a href="{% url 'student_update' student.id %}">
    Edit Student
</a>

</body>
</html>
""",

    "student_create.html": """<!DOCTYPE html>
<html>
<head>
    <title>Create Student</title>
</head>
<body>

<h1>Create Student</h1>

<form method="POST">

    {% csrf_token %}

    <label>Name:</label>
    <br>
    <input type="text" name="name" required>

    <br><br>

    <label>Roll No:</label>
    <br>
    <input type="number" name="roll_no" required>

    <br><br>

    <label>Email:</label>
    <br>
    <input type="email" name="email" required>

    <br><br>

    <label>Course:</label>
    <br>
    <input type="text" name="course" required>

    <br><br>

    <label>Age:</label>
    <br>
    <input type="number" name="age" required>

    <br><br>

    <button type="submit">
        Create Student
    </button>

</form>

<br>

<a href="{% url 'student_list' %}">
    Back to Student List
</a>

</body>
</html>
""",

    "student_update.html": """<!DOCTYPE html>
<html>
<head>
    <title>Update Student</title>
</head>
<body>

<h1>Update Student</h1>

<form method="POST">

    {% csrf_token %}

    <label>Name:</label>
    <br>
    <input
        type="text"
        name="name"
        value="{{ student.name }}"
        required
    >

    <br><br>

    <label>Roll No:</label>
    <br>
    <input
        type="number"
        name="roll_no"
        value="{{ student.roll_no }}"
        required
    >

    <br><br>

    <label>Email:</label>
    <br>
    <input
        type="email"
        name="email"
        value="{{ student.email }}"
        required
    >

    <br><br>

    <label>Course:</label>
    <br>
    <input
        type="text"
        name="course"
        value="{{ student.course }}"
        required
    >

    <br><br>

    <label>Age:</label>
    <br>
    <input
        type="number"
        name="age"
        value="{{ student.age }}"
        required
    >

    <br><br>

    <button type="submit">
        Update Student
    </button>

</form>

<br>

<a href="{% url 'student_list' %}">
    Cancel
</a>

</body>
</html>
""",

    "student_delete.html": """<!DOCTYPE html>
<html>
<head>
    <title>Delete Student</title>
</head>
<body>

<h1>Delete Student</h1>

<p>
    Are you sure you want to delete
    <strong>{{ student.name }}</strong>?
</p>

<p>
    Roll No: {{ student.roll_no }}
</p>

<form method="POST">

    {% csrf_token %}

    <button type="submit">
        Yes, Delete
    </button>

    <a href="{% url 'student_list' %}">
        Cancel
    </a>

</form>

</body>
</html>
"""
}


for filename, content in templates.items():

    file_path = template_dir / filename

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    print(f"Created: {file_path}")


print("\nAll template files created successfully!")