## Student Records API (Flask + SQLAlchemy)

A simple REST API built with **Flask** and **SQLAlchemy** to manage student records.  
Supports CRUD operations (Create, Read, Update, Delete) using a local SQLite database.
i will get it 

---

 Features
- **Add** a new student
- **Retrieve** all students or a specific student by ID
- **Update** student details (full update with PUT, partial update with PATCH)
- **Delete** a student
- Returns data in JSON format

---

 Requirements
Make sure you have Python **3.7+** installed.

Install dependencies:
```bash
pip install flask flask_sqlalchemy
````

---

 Setup & Run

1. Save the Python file as `Student_record.py`.
2. Initialize the database:

   ```python
   from app import db
   db.create_all()
   ```
3. Start the Flask app:

   ```bash
   flask run
   ```

   Or:

   ```bash
   python app.py
   ```
4. The API will be available at:

   ```
   http://127.0.0.1:5000/
   ```

---

 API Endpoints

Welcome Message

```
GET /
```

Response:

```json
"Welcome to student record!"
```

---

Get All Students

```
GET /students
```

Response Example:

```json
{
  "Students": [
    {
      "name": "John",
      "age": 15,
      "grade": "10th",
      "rollnumber": 23
    }
  ]
}
```

---

Get a Student by ID

```
GET /students/<id>
```

Response Example:

```json
{
  "name": "John",
  "age": 15,
  "grade": "10th",
  "rollnumber": 23
}
```

---

Add a New Student

```
POST /students
```
Request JSON:

```json
{
  "name": "Jane",
  "age": 14,
  "grade": "9th",
  "rollnumber": 12
}
```

Response Example:

```json
{
  "id": 1
}
```

---

Update a Student (Full Update)

```
PUT /students/<id>
```

Request JSON:

```json
{
  "name": "Jane Doe",
  "age": 15,
  "grade": "10th",
  "rollnumber": 12
}
```

Response Example:

```json
{
  "message": "updated Successfully!"
}
```

---

Update a Student (Partial Update)

```
PATCH /students/<id>
```

Request JSON Example:

```json
{
  "grade": "11th"
}
```

Response Example:

```json
{
  "message": "patched Successfully!"
}
```

---

Delete a Student

```
DELETE /students/<id>
```

Response Example:

```json
{
  "message": "yeet!@"
}
```


