# AI-Based Student Performance Prediction System

An AI and Machine Learning-based web application that predicts student academic performance, identifies weak areas, and provides personalized recommendations for improvement.

## Project Overview

The system analyzes academic and study-related data such as attendance, previous marks, assignments, internal marks, study hours, quiz scores, and other relevant factors to predict student performance.

It also supports **working students** by considering their work and study schedules instead of depending only on attendance.

The system can detect incomplete information, notify students and teachers, conduct syllabus-based quizzes, generate scorecards, identify weak topics, and track academic improvement.

---

## Key Features

* 🤖 **AI-Based Performance Prediction**
* 📋 **Student Information Completeness Check**
* 👨‍💼 **Working Student Support**
* 🔔 **Student & Teacher Notifications**
* 📝 **Syllabus-Based Quiz & Examination**
* 📊 **Automated Performance Scorecard**
* 🎯 **Weak Subject & Topic Identification**
* 💡 **Personalized Improvement Recommendations**
* 📈 **Progress & Improvement Tracking**
* ⚠️ **Early Academic Warning System**
* 🔄 **Retest and Performance Comparison**

---

## System Architecture

```text
Student / Teacher
       ↓
Django Web Application
       ↓
Information Validation
       ↓
Data Preprocessing
       ↓
Flask ML API
       ↓
Machine Learning Model
       ↓
Performance Prediction
       ↓
Weak Area Detection
       ↓
Syllabus-Based Quiz
       ↓
Scorecard
       ↓
Improvement Recommendation
       ↓
Progress Tracking
```

---

## How It Works

```text
Student Data
     ↓
Data Validation
     ↓
Missing Information Check
     ↓
ML Performance Prediction
     ↓
Identify Weak Areas
     ↓
Quiz / Examination
     ↓
Scorecard
     ↓
Improvement Recommendation
     ↓
Retest
     ↓
Track Improvement
```

---

## Technologies Used

| Technology          | Purpose              |
| ------------------- | -------------------- |
| Python              | Programming Language |
| Django              | Main Web Application |
| Flask               | ML API               |
| Pandas              | Data Processing      |
| NumPy               | Numerical Operations |
| Scikit-learn        | Machine Learning     |
| HTML/CSS/JavaScript | Frontend             |
| SQLite/PostgreSQL   | Database             |
| Git & GitHub        | Version Control      |

---

## Machine Learning

Possible algorithms:

* Decision Tree
* Random Forest
* Linear Regression
* Logistic Regression

### ML Pipeline

```text
Dataset
 ↓
Data Cleaning
 ↓
Preprocessing
 ↓
Feature Engineering
 ↓
Model Training
 ↓
Model Evaluation
 ↓
Best Model
 ↓
Prediction
```

---

## Performance Improvement

The system follows a continuous improvement cycle:

```text
Predict
  ↓
Assess
  ↓
Find Weak Areas
  ↓
Practice
  ↓
Retest
  ↓
Compare Results
  ↓
Track Improvement
```

Example:

```text
DBMS Quiz 1 → 60%
      ↓
Practice
      ↓
DBMS Quiz 2 → 75%
      ↓
Improvement: +15%
```

---

## Incomplete Information

If important student information is missing, the system can:

* Identify missing fields
* Notify the student
* Notify the teacher
* Request completion of required information
* Generate prediction after sufficient information is available

---

## Working Student Support

Working students can provide:

* Work status
* Working hours
* Study hours
* Academic performance
* Quiz and assignment scores

The system can then provide flexible assessments and personalized improvement recommendations.

---

## Project Structure

```text
AI-Based-Student-Performance-Prediction-System/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
├── datasets/
├── docs/
│   ├── Architecture.md
│   ├── Design.md
│   ├── Memory.md
│   ├── Phases.md
│   ├── PRD.md
│   └── Rules.md
│
├── scripts/
└── src/
```

---

## Development Phases

1. Project Setup
2. Dataset Collection & Preparation
3. ML Model Development
4. Flask ML API
5. Django Web Application
6. Student Data Validation
7. Prediction System
8. Quiz & Examination Module
9. Scorecard & Recommendations
10. Progress Tracking
11. Notifications & Early Warning
12. Dashboard & UI
13. Testing
14. Security & Optimization
15. Documentation & Deployment

---

## Security

* Secure authentication
* Password protection
* Input validation
* Role-based access
* Environment variables
* API protection
* Secure database access

---

## Future Scope

* AI-generated question papers
* Adaptive quizzes
* AI-powered study plans
* Explainable AI
* Parent/guardian reports
* Mobile application
* Email and push notifications
* Advanced academic analytics
* Cloud deployment
* LMS integration

---

## Documentation

* [`PRD.md`](PRD.md) — Project Requirements
* [`Architecture.md`](Architecture.md) — System Architecture
* [`Design.md`](Design.md) — UI/UX Design
* [`Phases.md`](Phases.md) — Development Phases
* [`Rules.md`](Rules.md) — Development Rules
* [`Memory.md`](Memory.md) — Project Progress

---

## Project Status

**Current Stage:** Project Setup & Planning

**Development Status:** In Progress

The project is being developed phase by phase, starting with dataset collection and Machine Learning model development.

---

## License

This project is developed for **educational and academic purposes**.
