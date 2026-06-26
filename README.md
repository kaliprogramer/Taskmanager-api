# 🚀 TaskManager API

A powerful and modern Task Management REST API built for productivity, automation, and scalable application development.

## 🌐 Live API

**Base URL**

```bash
https://taskmanager-api-4-7ff4.onrender.com/
```

This API provides secure JWT authentication, task management capabilities, and a Django Admin dashboard for full project administration.

---

## ✨ Features

* 🔐 JWT Authentication
* 👤 User Registration & Login
* ♻️ Refresh Access Tokens
* 📋 Create Tasks
* 📝 Update Tasks
* ❌ Delete Tasks
* 🔍 Retrieve Task Details
* 📚 List All Tasks
* 🛡 Protected Endpoints
* 🌍 RESTful API Architecture
* ⚡ Production Deployment on Render
* 🎯 Developer Friendly JSON Responses

---

## 🛠 Technology Stack

| Technology            | Purpose               |
| --------------------- | --------------------- |
| Python                | Backend Language      |
| Django                | Web Framework         |
| Django REST Framework | API Development       |
| JWT Authentication    | Secure Authentication |
| SQLite / Database     | Data Storage          |
| Render                | Cloud Deployment      |
| Postman               | API Testing           |

---

# 🔑 Authentication

This project uses JWT (JSON Web Token) authentication.

## Get Token

```http
POST /token/
```

Example Request

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Response

```json
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
```

---

## Refresh Token

```http
POST /token/refresh/
```

Example Request

```json
{
    "refresh": "your_refresh_token"
}
```

Response

```json
{
    "access": "new_access_token"
}
```

---

# 📋 Task API

## Get All Tasks

```http
GET /tasks/
```

Returns a list of all tasks.

---

## Get Single Task

```http
GET /tasks/{id}/
```

Returns a specific task.

---

## Create Task

```http
POST /tasks/
```

Example

```json
{
    "title": "Build AI Project",
    "description": "Finish object detection system",
    "completed": false
}
```

---

## Update Task

```http
PUT /tasks/{id}/
```

Example

```json
{
    "title": "Updated Task",
    "description": "New Description",
    "completed": true
}
```

---

## Partial Update

```http
PATCH /tasks/{id}/
```

---

## Delete Task

```http
DELETE /tasks/{id}/
```

---

# 📦 Example Task Object

```json
{
    "id": 1,
    "title": "Learn Django REST Framework",
    "description": "Build a production-ready API",
    "completed": false,
    "created_at": "2025-01-01T10:00:00Z"
}
```

---

# 🛡 Authentication Header

For protected routes include:

```http
Authorization: Bearer <access_token>
```

Example

```http
Authorization: Bearer eyJhbGciOiJIUz...
```

---

# 🎛 Admin Panel

Admin Dashboard

```bash
/admin/
```

### Credentials

```text
Username: kali
Password: kali
```

> For demonstration purposes only. Change credentials immediately in production environments.

---

# 🚀 Local Installation

Clone Repository

```bash
git clone https://github.com/kaliprogramer/Taskmanager-api.git
```

Enter Project

```bash
cd Taskmanager-api
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Start Server

```bash
python manage.py runserver
```

---

# 🧪 API Testing

Use:

* Postman
* Insomnia
* Thunder Client
* cURL

Example

```bash
curl -X GET \
https://taskmanager-api-4-7ff4.onrender.com/tasks/
```

---

# 📈 Future Improvements

* User-specific tasks
* Task categories
* Task priorities
* Due dates
* Search & filtering
* Email notifications
* AI-powered task suggestions
* WebSocket real-time updates

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Kiran (Kaliprogramer)**

Building APIs, AI systems, and developer tools one project at a time.
