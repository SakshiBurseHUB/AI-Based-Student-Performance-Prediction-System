#  AI-Based Student Performance Prediction System

An AI and Machine Learning-based web application that predicts student academic performance using student-related academic and study data.

---

##  Project Overview

The **AI-Based Student Performance Prediction System** analyzes student information such as attendance, study hours, previous marks, assignment marks, and internal marks.

A Machine Learning model uses this information to predict the student's expected academic performance.

The project uses:

* **Django** for the main web application
* **Flask** for the Machine Learning API
* **Python & Scikit-learn** for Machine Learning
* **Database** for storing student and prediction information

---

##  Objectives

* Predict student academic performance using Machine Learning.
* Analyze important factors affecting performance.
* Provide a simple web-based prediction system.
* Help teachers identify students who may need additional support.
* Display prediction results through a user-friendly dashboard.

---

##  System Architecture


                    User
                      ↓
                 Django Web App
                      ↓
                 Flask ML API
                      ↓
              Machine Learning Model
                      ↓
                  Prediction
                      ↓
                 Django Dashboard
                      ↓
                    User

---

##  How It Works


Student Data
     ↓
Data Preprocessing
     ↓
Machine Learning Model
     ↓
Performance Prediction
     ↓
Flask API
     ↓
Django Application
     ↓
Result Display
```

##  Technologies Used

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Main programming language |
| Django            | Main web application      |
| Flask             | ML prediction API         |
| Pandas            | Data processing           |
| NumPy             | Numerical operations      |
| Scikit-learn      | Machine Learning          |
| HTML              | Web structure             |
| CSS               | Web styling               |
| JavaScript        | Frontend interaction      |
| SQLite/PostgreSQL | Database                  |
| Git & GitHub      | Version control           |

##  Machine Learning

The system may use algorithms such as:

* Decision Tree
* Random Forest
* Linear Regression
* Logistic Regression

The final model will be selected based on its performance during testing.

### ML Process

```text
Dataset
   ↓
Data Cleaning
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model
   ↓
Prediction
---

##  Example Input

Attendance:       85%
Study Hours:      4 hours/day
Previous Marks:   78%
Assignment Marks: 82%
Internal Marks:   80%
```

### Example Output

Predicted Performance: HIGH
Expected Score: 82%
Status: Good Performance
```

> The actual prediction will depend on the trained Machine Learning model.

---

## 📁 Project Structure

AI-Based-Student-Performance-Prediction-System/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── data/
│   └── README.md
│
├── datasets/
│   └── README.md
│
├── docs/
│   ├── Architecture.md
│   ├── Design.md
│   ├── Memory.md
│   ├── Phases.md
│   ├── PRD.md
│   └── Rules.md
│
├── scripts/
│   └── README.md
│
└── src/
    └── README.md

The structure may be updated as the project develops.

---

##  Development Phases

1. Project Setup
2. Dataset & Data Analysis
3. Machine Learning Model
4. Flask ML API
5. Django Web Application
6. Django + Flask Integration
7. Dashboard & UI
8. Testing
9. Security & Optimization
10. Documentation & GitHub

---

##  Security

The project will follow basic security practices such as:

* Secure authentication
* Password protection
* Input validation
* Role-based access
* Environment variables for sensitive information
* Protection of API endpoints

---

##  Future Scope

Future improvements may include:

* Subject-wise performance prediction
* Early warning system
* Personalized study recommendations
* Advanced analytics
* Email notifications
* Explainable AI
* Mobile application
* Cloud deployment

---

##  Documentation

Detailed project documentation is available in:

* [`PRD.md`](PRD.md) — Project requirements
* [`Architecture.md`](Architecture.md) — System architecture
* [`Rules.md`](Rules.md) — Development rules
* [`Phases.md`](Phases.md) — Development phases
* [`Design.md`](Design.md) — UI/UX design
* [`Memory.md`](Memory.md) — Project progress

---

##  Project Status

**Current Stage:** Documentation & Planning

**Development Status:** Not Started

The project will be developed phase by phase.

---

##  License

This project is developed for **educational and academic purposes**.
