# AI-Based Student Performance Prediction System

## 1. Purpose

This document contains the rules that should be followed while developing the project.

The main goal is to keep the project:

* Simple
* Organized
* Secure
* Easy to understand
* Easy to maintain

---

## 2. General Rules

### Rule 1 — Follow the Project Structure

Keep Django, Flask, Machine Learning, database, and frontend code organized in their proper folders.

### Rule 2 — Don't Mix Responsibilities

```text
Django  → Web Application
Flask   → ML API
ML      → Model Training & Prediction
Database → Data Storage
```

Avoid putting all code into one file.

### Rule 3 — Keep Code Simple

Use simple and readable Python, HTML, CSS, and JavaScript.

Avoid unnecessary complexity.

### Rule 4 — Reuse Code

If the same functionality is required in multiple places, create a reusable function or component instead of copying the same code.

---

## 3. Django Rules

* Use Django models for database operations.
* Use forms for user input where appropriate.
* Keep views organized.
* Use templates for webpage presentation.
* Use Django authentication for login.
* Do not store passwords manually.
* Keep secrets out of source code.

---

## 4. Flask Rules

* Flask should mainly handle the ML prediction API.
* Use clear API routes.
* Validate incoming data.
* Return proper JSON responses.
* Handle errors properly.
* Do not duplicate Django functionality inside Flask.

---

## 5. Machine Learning Rules

### Dataset

* Use a reliable dataset.
* Do not modify original data unnecessarily.
* Keep a copy of the original dataset.
* Document important dataset features.

### Preprocessing

* Handle missing values.
* Remove duplicate or invalid records.
* Use appropriate feature preprocessing.
* Avoid data leakage.

### Model Training

* Split data into training and testing sets.
* Test more than one suitable algorithm when possible.
* Compare model performance.
* Select the best suitable model.

### Model Saving

Save the final trained model in a separate model directory.

Example:

```text
models/
└── student_performance_model.pkl
```

---

## 6. Database Rules

* Use meaningful model and field names.
* Avoid duplicate data where possible.
* Use migrations for Django database changes.
* Do not delete important data without checking.
* Keep database configuration secure.

---

## 7. Security Rules

The project must:

* Protect passwords.
* Validate user input.
* Restrict unauthorized access.
* Protect API endpoints.
* Never expose secret keys.
* Never commit `.env` files containing secrets.
* Use environment variables for sensitive configuration.

Example:

```text
.env
```

should not be uploaded to GitHub.

---

## 8. Git & GitHub Rules

### Commit Regularly

Make commits after completing meaningful work.

Example:

```text
git add .
git commit -m "Add student prediction model"
git push
```

### Commit Messages

Use clear messages.

Good:

```text
Add student model
Create prediction API
Update dashboard
Fix login validation
```

Avoid:

```text
update
changes
abc
final
final2
```

### Do Not Upload

Never commit:

```text
.env
__pycache__/
*.pyc
venv/
.venv/
database files containing sensitive data
```

Use `.gitignore`.

---

## 9. Testing Rules

Every major feature should be tested.

Examples:

* Login testing
* Student data validation
* Database testing
* API testing
* ML prediction testing
* Dashboard testing
* Error handling testing

Fix errors before moving to the next major phase.

---

## 10. UI/UX Rules

The interface should be:

* Simple
* Clean
* Responsive
* Easy to navigate
* Consistent

Use the same:

* Colors
* Fonts
* Buttons
* Spacing
* Cards
* Navigation style

throughout the application.

Detailed design rules will be maintained in `Design.md`.

---

## 11. Documentation Rules

Update documentation when major changes are made.

Important files:

```text
PRD.md
Architecture.md
Rules.md
Phases.md
Design.md
Memory.md
README.md
```

`Memory.md` should always show:

* What is completed
* What is currently being developed
* What comes next
* Important changes or decisions

---

## 12. Development Rules

### Always

* Understand the existing code before changing it.
* Test changes after implementation.
* Keep files organized.
* Update documentation.
* Commit working changes to GitHub.

### Avoid

* Randomly changing working code.
* Creating unnecessary files.
* Duplicating code.
* Hardcoding passwords or API keys.
* Skipping testing.
* Making major changes without updating documentation.

---

## 13. Project Quality Rule

Before considering a feature complete:

```text
Code
 ↓
Test
 ↓
Fix Errors
 ↓
Verify
 ↓
Document
 ↓
Git Commit
```