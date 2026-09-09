# AI-Based Student Performance Prediction System

## 1. Project Overview

**Project Name:** AI-Based Student Performance Prediction System

**Purpose:**
The system uses **Machine Learning** to predict a student's academic performance based on academic and study-related information.

**Main Technologies:**

* Python
* Django
* Flask
* Machine Learning
* Pandas
* NumPy
* Scikit-learn
* HTML, CSS, JavaScript
* SQLite/PostgreSQL

---

## 2. Problem Statement

It is difficult for teachers to manually analyze many students and identify students who may have poor academic performance.

This project uses Machine Learning to analyze student data and predict their expected performance.

---

## 3. Objectives

* Collect student academic data.
* Analyze and preprocess the data.
* Train a Machine Learning model.
* Predict student performance.
* Provide a simple web interface.
* Help teachers identify students who may need additional support.
* Display prediction results through a dashboard.

---

## 4. Target Users

### Student

* View academic information.
* Enter required information.
* Get performance prediction.
* View prediction results.

### Teacher

* View student information.
* View student predictions.
* Identify students who may need support.

### Administrator

* Manage users.
* Manage student records.
* Manage system data.

---

## 5. Main Features

### User Management

* Registration
* Login
* Logout
* Role-based access

### Student Management

* Add student information.
* View and update academic records.
* Store student performance data.

### Performance Prediction

The system will use information such as:

* Attendance
* Study hours
* Previous marks
* Assignment marks
* Internal marks

The Machine Learning model will predict the student's performance.

### Dashboard

The dashboard can display:

* Total students
* Performance categories
* Prediction results
* Charts and statistics

---

## 6. Django and Flask Roles

### Django

Django will be used for the **main web application**.

It will handle:

* Users
* Student data
* Database
* Dashboard
* Web pages
* Prediction results

### Flask

Flask will be used for the **Machine Learning API**.

It will:

1. Receive student data from Django.
2. Load the trained ML model.
3. Generate the prediction.
4. Send the result back to Django.

```text
User
 ↓
Django
 ↓
Flask API
 ↓
ML Model
 ↓
Prediction
 ↓
Django Dashboard
```

---

## 7. Machine Learning

The project will use a suitable Machine Learning algorithm such as:

* Decision Tree
* Random Forest
* Linear Regression
* Logistic Regression

The final algorithm will be selected after testing the models.

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
```

---

## 8. Expected Output

The system should provide a prediction such as:

```text
Student: Rahul

Predicted Performance: HIGH
Expected Score: 82%
Status: Good Performance
```

The exact output will depend on the final Machine Learning model.

---

## 9. Project Scope

The project will include:

* Student data management
* Machine Learning prediction
* Django web application
* Flask ML API
* Database
* Dashboard
* Prediction results
* Basic data visualization

---

## 10. Expected Outcome

The final system will provide a working web application that can analyze student information and predict academic performance using Machine Learning.

The prediction can help students and teachers understand possible performance levels and identify students who may require additional academic support.

