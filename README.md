# Django REST Framework – Rate Limiter & CSV Upload Project

This project demonstrates how to implement a **custom rate limiter using Redis** in Django REST Framework and how to **upload and process CSV files** safely into the database.

The goal is to:
- Prevent API abuse using rate limiting
- Handle large CSV uploads
- Avoid duplicate data insertion using unique constraints
- Learn real-world backend patterns

---

## 📌 Features

- ✅ Custom Rate Limiter using Redis
- ✅ Per-user / per-IP throttling
- ✅ Per-endpoint rate limiting
- ✅ CSV file upload and parsing
- ✅ Safe database inserts using `get_or_create`
- ✅ PostgreSQL / SQLite compatible
- ✅ Beginner-friendly architecture

---

## 🧠 How Rate Limiting Works (Simple Explanation)

Each request:
1. Generates a Redis key based on:
   - User ID (or IP for anonymous users)
   - API endpoint
2. Redis stores:
   - Request count
   - Expiry time (TTL)
3. If requests exceed the limit before expiry:
   - API returns **429 Too Many Requests**
4. When TTL expires:
   - Redis automatically resets the counter

Redis is used because it is **fast**, **atomic**, and **auto-cleans expired keys**.

---

## 🏗️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- Redis
- PostgreSQL / SQLite
- CSV module

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```
## Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

