# 🌐 Personal Profile Web App (Flask + Docker)

This is a simple profile page built using Flask and Docker. It includes:

- A profile photo
- A short introduction
- A message box that triggers a JavaScript alert with the message
- A "Say Hello" feature that greets the user by name

## 🛠️ Tech Stack

- Python 3.10
- Flask
- HTML + CSS + JavaScript
- Docker

## 🐳 Run with Docker (Port: 5007)

```bash
docker build -t flask-profile-app .
docker run -d -p 5007:5007 flask-profile-app

http://localhost:5007
```
