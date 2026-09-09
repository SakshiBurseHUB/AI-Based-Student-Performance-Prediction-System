# AI-Based Student Performance Prediction System

## 1. Purpose

This document explains the **application flow, system architecture, and folder structure** of the project.

The project uses:

* **Django** → Main web application
* **Flask** → Machine Learning API
* **Python + Scikit-learn** → Machine Learning
* **Database** → Store student and prediction data

---

## 2. Basic Architecture

```text
              User
                ↓
        ┌───────────────┐
        │    Django     │
        │   Web App     │
        └───────┬───────┘
                │
        Student Data
                ↓
        ┌───────────────┐
        │    Flask      │
        │    ML API     │
        └───────┬───────┘
                │
                ↓
        ┌───────────────┐
        │  ML Model     │
        │ Scikit-learn  │
        └───────┬───────┘
                │
                ↓
          Prediction
                │
                ↓
        ┌───────────────┐
        │    Django     │
        │   Dashboard   │
        └───────────────┘
```

---

## 3. Application Flow

### Step 1 — User Login

The user logs into the Django application.

```text
User → Django → Login → Dashboard
```

### Step 2 — Enter Student Data

The user enters required information such as:

* Attendance
* Study hours
* Previous marks
* Assignment marks
* Internal marks

### Step 3 — Send Data to Flask

Django sends the student data to the Flask API.

```text
Django → Flask API
```

### Step 4 — Machine Learning Prediction

Flask sends the data to the trained ML model.

```text
Flask → ML Model → Prediction
```

### Step 5 — Return Result

Flask sends the prediction back to Django.

```text
Flask → Django
```

### Step 6 — Display Result

Django displays the prediction on the dashboard.

```text
Prediction → Django Dashboard → User
```

---

## 4. Project Structure

The final project will follow a structure similar to:

```text
AI-Based-Student-Performance-Prediction-System/
│
├── django_app/
│   ├── manage.py
│   ├── users/
│   ├── students/
│   ├── predictions/
│   ├── templates/
│   └── static/
│
├── flask_api/
│   ├── app.py
│   ├── model/
│   └── routes/
│
├── ml/
│   ├── dataset/
│   ├── notebooks/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── models/
│   └── student_performance_model.pkl
│
├── docs/
│
├── PRD.md
├── Architecture.md
├── Rules.md
├── Phases.md
├── Design.md
├── Memory.md
├── README.md
└── requirements.txt
```

> The exact folder structure may be updated during development.

---

## 5. Main Components

### Django Application

Responsible for:

* Login and registration
* Student management
* Database operations
* Forms
* Dashboard
* Sending prediction requests
* Displaying results

### Flask API

Responsible for:

* Receiving prediction requests
* Loading the ML model
* Processing prediction input
* Returning prediction results

### Machine Learning

Responsible for:

* Dataset processing
* Feature selection
* Model training
* Model evaluation
* Performance prediction

### Database

Responsible for storing:

* User information
* Student information
* Academic records
* Prediction history

---

## 6. Data Flow

```text
Student Information
        ↓
      Django
        ↓
    Flask API
        ↓
   ML Model
        ↓
   Prediction
        ↓
      Django
        ↓
     Database
        ↓
    Dashboard
```

---

## 7. Communication Between Django and Flask

Django and Flask will communicate using an **HTTP API**.

Example:

```text
Django
   │
   │ POST student data
   ↓
Flask API
   │
   │ ML prediction
   ↓
Flask API
   │
   │ JSON result
   ↓
Django
```

Example response:

```json
{
    "prediction": "High Performance",
    "score": 82
}
```

---

## 8. Database Flow

```text
User
 ↓
Django
 ↓
Database
 ↓
Student Data
 ↓
Prediction
 ↓
Prediction History
```

---

## 9. Security

The application should include:

* User authentication
* Password protection
* Role-based access
* Input validation
* CSRF protection
* Secure API communication
* Protection of sensitive configuration

---

## 10. Architecture Principle

The project follows a **separation of responsibilities**:

```text
Django  → Web Application
Flask   → ML API
ML      → Prediction
Database → Data Storage
