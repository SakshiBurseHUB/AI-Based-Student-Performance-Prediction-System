# AI-Based Student Performance Prediction System

An AI and Machine Learning-based web application designed to predict student academic performance, identify areas requiring improvement, and provide personalized academic support through syllabus-based quizzes, assessments, scorecards, and progress tracking.

---

## Project Overview

The **AI-Based Student Performance Prediction System** is a web-based academic support platform that uses Machine Learning to analyze student-related academic and study data and predict expected academic performance.

The system is designed to support both **regular students and working students** who may have limited time or college attendance.

Instead of depending on a single factor such as attendance, the system considers multiple academic and behavioral parameters such as:

* Attendance
* Study hours
* Previous examination marks
* Assignment marks
* Internal assessment marks
* Quiz and test performance
* Subject-wise performance
* Academic progress
* Work status and working hours

The system also handles incomplete student information. If important information is missing, the system can notify the student and teacher to complete the required academic records before generating a reliable prediction.

After prediction, the system can identify weak subjects or topics and conduct **syllabus-based quizzes and examinations**. The results are presented through a scorecard, allowing students and teachers to monitor improvement over time.

---

## Key Features

### 1. AI-Based Performance Prediction

The Machine Learning model analyzes student academic information and predicts expected academic performance.

### 2. Student Information Completeness Check

The system checks whether the required student academic information has been provided.

If important information is missing:

* The student is notified.
* The teacher is notified.
* Missing information is identified.
* Prediction can be restricted until the required information is completed.

### 3. Support for Working Students

The system is designed to support students who are working while studying.

Working students can provide information such as:

* Work status
* Working hours
* Study hours
* Attendance
* Academic performance
* Assignment completion
* Internal marks

The system does not depend only on attendance and can use multiple academic indicators for prediction.

It can also provide flexible improvement activities such as short quizzes, topic-wise tests, and revision recommendations.

### 4. Syllabus-Based Quiz and Examination

The system can conduct quizzes and examinations based on the student's academic syllabus.

Possible assessment types include:

* Subject-wise quizzes
* Topic-wise quizzes
* Chapter-wise tests
* Short assessments
* Practice examinations
* Full-length examinations

### 5. Automated Scorecard

After completing a quiz or examination, the system generates a scorecard containing information such as:

* Total questions
* Correct answers
* Incorrect answers
* Score
* Percentage
* Subject performance
* Topic performance
* Performance level

Example:

```text
-----------------------------------
        QUIZ PERFORMANCE
-----------------------------------

Subject: DBMS

Total Questions:     20
Correct Answers:     16
Incorrect Answers:    4
Score:               80%

Performance:         GOOD

Weak Topics:
- Normalization
- Transactions

Recommendation:
Practice more questions from
the identified weak topics.
-----------------------------------
```

### 6. Weak Subject and Topic Identification

The system analyzes assessment results to identify subjects and topics where the student requires improvement.

For example:

```text
DBMS
 ├── SQL                  85%  ✓
 ├── Normalization        55%  ⚠
 ├── Transactions         60%  ⚠
 └── ER Model             82%  ✓
```

This helps students focus their limited study time on the areas that need the most attention.

### 7. Personalized Improvement Recommendations

Based on prediction results and quiz performance, the system can recommend:

* Topics to study
* Subjects requiring attention
* Additional practice
* Revision activities
* Recommended quizzes
* Assignment completion
* Study targets
* Exam preparation

For working students, recommendations can be adapted around their available study time.

### 8. Progress Tracking

Students can attempt assessments multiple times and track their improvement.

Example:

```text
DBMS Quiz 1     → 60%
       ↓
Practice
       ↓
DBMS Quiz 2     → 72%
       ↓
Revision
       ↓
DBMS Quiz 3     → 84%
```

The dashboard can display performance trends to show whether the student's academic performance is improving.

### 9. Early Academic Warning

The system can identify students whose predicted performance is declining.

For example:

```text
⚠ Academic Performance Alert

Student performance has decreased
compared with the previous assessment.

Recommended Action:
Additional practice and academic
support are suggested.
```

Teachers can use these alerts to identify students who may require additional academic support.

### 10. Student and Teacher Notifications

The system can notify students and teachers about:

* Missing information
* Pending assessments
* Poor quiz performance
* Weak subjects
* Declining performance
* Recommended practice
* Improvement opportunities

---

## Objectives

* Predict student academic performance using Machine Learning.
* Analyze multiple factors affecting student performance.
* Support both regular and working students.
* Detect incomplete student academic information.
* Notify students and teachers about missing information.
* Identify weak subjects and topics.
* Conduct syllabus-based quizzes and examinations.
* Generate automated performance scorecards.
* Provide personalized improvement recommendations.
* Track student performance over multiple assessments.
* Help teachers identify students who may require additional support.
* Provide a user-friendly academic performance dashboard.

---

## System Architecture

```text
                    Student / Teacher
                           ↓
                  Django Web Application
                           ↓
                 Student Information Check
                           ↓
                ┌──────────┴──────────┐
                ↓                     ↓
        Information Missing      Information Complete
                ↓                     ↓
       Notify Student/Teacher   Data Preprocessing
                                      ↓
                             Machine Learning Model
                                      ↓
                              Performance Prediction
                                      ↓
                         ┌────────────┴────────────┐
                         ↓                         ↓
                 Prediction Result          Weak Area Detection
                                                   ↓
                                          Syllabus-Based Quiz
                                                   ↓
                                             Scorecard
                                                   ↓
                                    Improvement Recommendation
                                                   ↓
                                           Progress Tracking
                                                   ↓
                                      Updated Performance
```

---

## How It Works

```text
Student Academic Data
        ↓
Data Validation
        ↓
Information Completeness Check
        ↓
Missing Data?
   ↓              ↓
  YES             NO
   ↓               ↓
Notify Student   Data Preprocessing
& Teacher             ↓
                     ML Model
                       ↓
               Performance Prediction
                       ↓
                Identify Weak Areas
                       ↓
             Syllabus-Based Assessment
                       ↓
                   Scorecard
                       ↓
             Improvement Recommendation
                       ↓
                Progress Tracking
                       ↓
              Reassessment / Retest
                       ↓
             Updated Performance
```

---

## Technologies Used

| Technology          | Purpose                         |
| ------------------- | ------------------------------- |
| Python              | Main programming language       |
| Django              | Main web application            |
| Flask               | Machine Learning prediction API |
| Pandas              | Data processing                 |
| NumPy               | Numerical operations            |
| Scikit-learn        | Machine Learning                |
| HTML5               | Web structure                   |
| CSS3                | Web styling                     |
| JavaScript          | Frontend interaction            |
| SQLite / PostgreSQL | Database                        |
| Git & GitHub        | Version control                 |

---

## Machine Learning

The system may evaluate different Machine Learning algorithms, including:

* Decision Tree
* Random Forest
* Linear Regression
* Logistic Regression

The final algorithm will be selected based on its performance during model evaluation.

### ML Process

```text
Dataset
   ↓
Data Collection
   ↓
Data Cleaning
   ↓
Missing Value Handling
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Performance Prediction
```

---

## Student Performance Factors

The system can consider several factors rather than depending on a single parameter.

| Factor              | Example               |
| ------------------- | --------------------- |
| Attendance          | 75%                   |
| Study Hours         | 3 hours/day           |
| Previous Marks      | 78%                   |
| Assignment Marks    | 82%                   |
| Internal Marks      | 80%                   |
| Quiz Score          | 75%                   |
| Previous GPA/CGPA   | 7.2                   |
| Work Status         | Working / Not Working |
| Working Hours       | 8 hours/day           |
| Subject Performance | Subject-wise scores   |

The exact features will depend on the final dataset and trained Machine Learning model.

---

## Example Input

```text
Attendance:        75%
Study Hours:       3 hours/day
Previous Marks:    78%
Assignment Marks:  82%
Internal Marks:    80%
Quiz Score:        76%
Work Status:       Working
Working Hours:     8 hours/day
```

### Example Output

```text
Predicted Performance: HIGH

Expected Score: 82%

Status: Good Performance

Data Completeness: 100%
Prediction Confidence: High
```

> The actual prediction will depend on the trained Machine Learning model and available data.

---

## Example: Incomplete Information

If required information is missing:

```text
Student Information

Previous Marks:     78%       ✓
Assignment Marks:   82%       ✓
Internal Marks:     —         ✗
Quiz Score:         76%       ✓
Attendance:         —         ✗
```

The system can display:

```text
⚠ Information Incomplete

Required academic information is missing.

Please complete the missing information
before generating the performance prediction.

Notifications sent to:
✓ Student
✓ Teacher
```

---

## Example: Improvement Scorecard

```text
====================================
       ACADEMIC IMPROVEMENT CARD
====================================

Student: Student A

Subject       Score       Status
------------------------------------
DBMS           60%       Improve
DAA            78%       Good
DCN            85%       Excellent
Web Dev        90%       Excellent

Weak Topics:
• DBMS Normalization
• DBMS Transactions

Recommended Action:
• Practice DBMS questions
• Revise weak topics
• Attempt the next DBMS quiz

Previous Score:     60%
Current Score:      78%

Improvement:        +18%
====================================
```

---

## Working Student Support

A major goal of the system is to provide academic support to students who are working while studying.

Instead of treating low attendance as the only indicator of poor performance, the system considers multiple factors.

```text
Working Student
      ↓
Work Hours + Study Hours
      ↓
Academic Performance Data
      ↓
AI Performance Prediction
      ↓
Identify Weak Areas
      ↓
Short / Flexible Quiz
      ↓
Scorecard
      ↓
Personalized Improvement Plan
      ↓
Progress Tracking
```

Possible support includes:

* Short topic-wise quizzes
* Flexible assessments
* Weekend practice tests
* Subject-wise revision
* Weak-topic recommendations
* Assignment reminders
* Progress tracking
* Early academic alerts

---

## 📈 Performance Improvement Cycle

The system follows a continuous improvement approach:

```text
Predict
   ↓
Assess
   ↓
Identify Weak Areas
   ↓
Practice
   ↓
Retest
   ↓
Compare Results
   ↓
Track Improvement
   ↓
Update Prediction
```

This makes the system more than a prediction tool. It becomes an **academic performance improvement platform**.

---

## 📁 Project Structure

```text
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
```

The structure will be updated as development progresses.

---

## Development Phases

1. Project Setup
2. Dataset Collection
3. Data Cleaning and Analysis
4. Machine Learning Model
5. Flask ML API
6. Django Web Application
7. Django + Flask Integration
8. Student Information Validation
9. Student and Teacher Notification System
10. Student Performance Prediction
11. Syllabus and Question Bank Module
12. Quiz and Examination Module
13. Automated Scorecard
14. Weak Subject and Topic Detection
15. Personalized Improvement Recommendations
16. Progress Tracking and Retest
17. Early Academic Warning System
18. Dashboard & UI
19. Testing
20. Security & Optimization
21. Documentation & GitHub
22. Deployment

---

## Security

The project will follow basic security practices such as:

* Secure authentication
* Password protection
* Input validation
* Role-based access
* Environment variables for sensitive information
* Protection of API endpoints
* Secure database access
* Authorization for student and teacher features
* Validation of quiz and academic data

---

## Future Scope

Future improvements may include:

* Advanced subject-wise performance prediction
* AI-generated question papers
* Adaptive quizzes based on student performance
* Automatic difficulty adjustment
* AI-powered study plans
* Explainable AI
* Natural Language Processing-based academic assistance
* Email and push notifications
* Parent/guardian performance reports
* Mobile application
* Cloud deployment
* Advanced academic analytics
* Integration with Learning Management Systems (LMS)
* Real-time teacher dashboards

---

## Documentation

Detailed project documentation is available in:

* [`PRD.md`](PRD.md) — Project requirements
* [`Architecture.md`](Architecture.md) — System architecture
* [`Rules.md`](Rules.md) — Development rules
* [`Phases.md`](Phases.md) — Development phases
* [`Design.md`](Design.md) — UI/UX design
* [`Memory.md`](Memory.md) — Project progress

---

## Project Status

**Current Stage:** Project Setup & Planning

**Development Status:** In Progress

The project will be developed phase by phase, beginning with dataset collection and preparation, followed by Machine Learning model development and web application integration.

---

## License

This project is developed for **educational and academic purposes**.
