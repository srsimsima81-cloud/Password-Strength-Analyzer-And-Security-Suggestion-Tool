# 🔐 Password Strength Analyzer & Security Suggestion Tool

> **Defensive Cybersecurity Project**  
> A local password assessment and security education tool that analyzes password strength, identifies common and predictable patterns, provides actionable security suggestions, evaluates configurable password policies, and generates secure demo passwords.

---

## 📌 Overview

**Password Strength Analyzer** is a locally hosted defensive cybersecurity application designed to demonstrate fundamental password-security concepts through practical analysis.

The application evaluates a password using multiple factors rather than relying on password length alone. It examines:

- Password length
- Character diversity
- Character uniqueness
- Common-password usage
- Keyboard patterns
- Sequential patterns
- Repeated characters and substrings
- Predictable structures
- Dictionary words
- Date and year patterns
- Optional personal-information overlap
- Theoretical entropy
- Configurable password-policy requirements

The project also includes a **secure password generator**, **password-policy checker**, **aggregate security analytics dashboard**, and an educational section covering real-world password-security practices.

> **Important:** The scoring system is an educational model created for this project. It is not a universal password-strength standard and does not claim to predict an exact password-cracking time.

---

## 🎯 Project Objectives

1. Demonstrate defensive password-security concepts.
2. Identify weak and predictable password patterns.
3. Show why password length alone does not determine security.
4. Demonstrate the risks of common and reused passwords.
5. Detect predictable personal information in passwords.
6. Provide actionable security recommendations.
7. Demonstrate secure random password generation using Python `secrets`.
8. Demonstrate configurable password policies.
9. Store only safe aggregate analytics rather than passwords.
10. Provide an educational cybersecurity dashboard suitable for academic and portfolio use.

---

## 🛡️ Defensive Security Scope

This project is intentionally designed for **defensive cybersecurity education**.

### Included

- Local password analysis
- Password-strength assessment
- Common-password detection
- Pattern detection
- Personal-information detection
- Password-policy checking
- Secure password generation
- Aggregate security analytics
- Password-security education
- Synthetic demonstration data
- Local Argon2id hashing demonstration

### Not Included

- Password cracking
- Credential theft
- Credential collection
- Brute-force attacks
- Dictionary attacks against real accounts
- Password dumping
- Credential stuffing
- Phishing
- Real leaked-password datasets
- External password analysis services

The application does not transmit analyzed passwords to third-party services.

---

## 🏗️ Architecture

```text
┌─────────────────────────────────────────────┐
│              Web Interface                  │
│        HTML + CSS + JavaScript              │
└──────────────────────┬──────────────────────┘
                       │
                       │ Local HTTP
                       ▼
┌─────────────────────────────────────────────┐
│               Flask Backend                 │
│                  app.py                     │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│          Password Analysis Engine           │
├─────────────────────────────────────────────┤
│ Length Analyzer                             │
│ Character Analyzer                          │
│ Pattern Detector                            │
│ Common Password Checker                     │
│ Context Checker                             │
│ Entropy Estimator                            │
│ Scoring Engine                              │
│ Suggestion Engine                           │
│ Password Policy Checker                     │
└──────────────────────┬──────────────────────┘
                       │
              Safe aggregate metadata
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              SQLite Database                │
│        Aggregate Analysis Metadata          │
└─────────────────────────────────────────────┘
```

---

## 🧰 Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

### Backend

- Python
- Flask

### Database

- SQLite

### Security

- Python `secrets`
- Argon2id demonstration using `argon2-cffi`

### Testing

- Pytest

---

## ✨ Features

### 🔎 Password Analysis

The analyzer evaluates multiple characteristics of a password:

- Length
- Uppercase characters
- Lowercase characters
- Numbers
- Symbols
- Spaces
- Character-type diversity
- Unique-character ratio
- Sequential patterns
- Keyboard patterns
- Repeated characters
- Repeated substrings
- Predictable structures
- Dictionary words
- Year/date patterns
- Common passwords
- Optional personal information
- Theoretical entropy

---

### 📊 Strength Classification

The project uses five educational strength categories:

| Score | Classification |
|---:|---|
| 0–20 | VERY WEAK |
| 21–40 | WEAK |
| 41–60 | MODERATE |
| 61–80 | STRONG |
| 81–100 | VERY STRONG |

These ranges are **project-defined educational bands**, not an industry-wide standard.

---

### 💡 Security Suggestions

The application provides recommendations based on detected weaknesses.

Examples include:

- Use a longer password or passphrase.
- Avoid commonly used passwords.
- Avoid keyboard sequences.
- Avoid predictable number sequences.
- Avoid repeated characters.
- Avoid predictable years and dates.
- Avoid personal information.
- Avoid password reuse.
- Consider using a password manager.
- Enable multi-factor authentication.

---

### 🔐 Secure Password Generator

The application includes a configurable password generator.

It supports:

- Uppercase letters
- Lowercase letters
- Numbers
- Symbols
- Configurable password length

Randomness is generated using Python's `secrets` module rather than the ordinary `random` module.

Generated passwords are not stored in the database.

---

### 🧑‍💻 Personal Information Detection

Optional context can be supplied using synthetic demonstration values:

- First Name
- Birth Year
- Company / College Name

For example:

```text
Password: Alex1998!

First Name: Alex
Birth Year: 1998
Company / College: Northbridge College
```

The analyzer can identify the use of personal information as a predictable password characteristic.

These context values are processed for analysis and are **not persisted**.

---

### 📋 Password Policy Checker

The project includes a separate password-policy evaluation system.

Configurable policy options include:

- Minimum password length
- Reject common passwords
- Reject personal information

The policy result is presented separately from the numerical strength score.

This distinction demonstrates that:

> **Password strength assessment and password-policy compliance are related but different concepts.**

---

### 📈 Aggregate Analytics Dashboard

The dashboard displays security statistics without exposing passwords.

Example metrics include:

- Total analyses
- Average score
- Strength distribution
- Score distribution
- Aggregate weakness information

The database stores analysis metadata such as:

```text
Score
Classification
Password length
Unique-character ratio
Weakness count
Timestamp
```

It does **not** contain a password field.

---

## 🔒 Privacy & Security Design

A core design requirement of this project is preventing unnecessary password exposure.

### Passwords are not:

- Stored in SQLite
- Written to application logs
- Saved to files
- Added to browser storage
- Sent to third-party password-analysis services
- Included in analytics records

### Personal context is not persisted

Optional fields such as:

```text
First Name
Birth Year
Company / College
```

are used only during the current analysis.

### Analytics contain metadata only

The database is deliberately designed without a password column.

This demonstrates an important security principle:

> **Do not retain sensitive credentials when they are not required for the application's purpose.**

---

## 🗄️ Database Design

The application uses SQLite for local aggregate analytics.

Conceptually:

```text
ANALYSES
────────────────────────────
analysis_id
score
classification
password_length
unique_character_ratio
weakness_count
created_at
```

No plaintext password is stored.

The database is intended for educational analytics rather than credential storage.

---

## 🧠 Password Security Concepts Demonstrated

### Password Length

Longer passwords generally provide more possible combinations, but length alone does not guarantee strength.

For example:

```text
aaaaaaaaaaaaaaaa
```

is long but highly predictable.

---

### Character Diversity

Using multiple character types can increase the theoretical search space.

The analyzer considers:

- lowercase
- uppercase
- digits
- symbols
- spaces

However, simply adding `123!` to a predictable word does not automatically create a strong password.

---

### Predictable Patterns

The project identifies patterns such as:

```text
123456
abcdef
qwerty
welcome123
Password123!
```

These patterns are important because human-created passwords often contain predictable structures.

---

### Personal Information

Passwords containing information such as names or birth years can be easier to guess when that information is known or discoverable.

Example:

```text
Alex1998!
```

when the corresponding context is:

```text
First Name: Alex
Birth Year: 1998
```

---

### Entropy

The application provides a theoretical entropy-style estimate based on password length and detected character pools.

This is explicitly presented as an **estimate**, because human password choices are often not random.

Therefore:

> A theoretical entropy calculation should not be interpreted as an exact measurement of real-world password security.

---

## 🔑 Password Hashing Demonstration

The project includes a separate educational Argon2id hashing demonstration.

Argon2id is designed for securely storing passwords in authentication systems.

Conceptually:

```text
User Password
      │
      ▼
   Argon2id
      │
      ▼
Password Hash
      │
      ▼
Database
```

The hashing demonstration is intentionally separate from the password analyzer.

The analyzer does **not** store analyzed passwords.

---

## 🧪 Testing

The project includes automated tests using Pytest.

Run:

```powershell
pytest -q
```

The test suite covers:

- Empty password handling
- Common-password detection
- Keyboard patterns
- Sequential patterns
- Repetition detection
- Predictable structures
- Personal-information detection
- Password length analysis
- Secure password generation
- Password non-disclosure in analyzer results
- API health
- API password non-disclosure
- Generator API

Current automated test result:

```text
10 passed
```

---

## 🧪 Primary Demonstration Cases

### Case 1 — Very Weak

```text
123456
```

Demonstrates:

- Very short password
- Common password detection
- Weakness suggestions

---

### Case 2 — Personal Information

```text
Password: Alex1998!
First Name: Alex
Birth Year: 1998
```

Demonstrates:

- Personal-information detection
- Predictable structure detection
- Security suggestions

Use synthetic information only.

---

### Case 3 — Strong Password

```text
V7!qR2@zL9#pT4$x
```

Demonstrates:

- Longer length
- Character diversity
- High uniqueness
- Absence of obvious predictable patterns

For real accounts, use a password generated specifically for that account rather than copying a demonstration password.

---

## 📂 Project Structure

```text
Password-Strength-Analyzer/
│
├── backend/
│   ├── app.py
│   │
│   ├── services/
│   │   ├── password_analyzer.py
│   │   ├── length_analyzer.py
│   │   ├── character_analyzer.py
│   │   ├── pattern_detector.py
│   │   ├── common_password_checker.py
│   │   ├── entropy_estimator.py
│   │   ├── scoring_engine.py
│   │   ├── suggestion_engine.py
│   │   ├── password_generator.py
│   │   ├── context_checker.py
│   │   └── policy_checker.py
│   │
│   ├── models/
│   │   └── database.py
│   │
│   └── utils/
│       └── hashing_demo.py
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── data/
│   └── common_passwords.txt
│
├── tests/
│   ├── test_analyzer.py
│   └── test_api.py
│
├── docs/
│   ├── PROJECT_GUIDE.md
│   ├── TEST_PLAN.md
│   └── INTERVIEW_PREP.md
│
├── reports/
│   └── PROJECT_REPORT.md
│
├── screenshots/
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```powershell
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Password-Strength-Analyzer
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Run the tests

```powershell
pytest -q
```

### 6. Start the application

```powershell
py backend\app.py
```

### 7. Open the application

```text
http://127.0.0.1:5000
```

---

## 🖥️ Local Execution

The application is designed to run locally.

```text
Browser
   │
   ▼
127.0.0.1:5000
   │
   ▼
Flask Application
   │
   ├── Password Analysis
   ├── Policy Evaluation
   ├── Secure Generation
   └── Aggregate Analytics
           │
           ▼
       SQLite
```

No cloud account is required for the basic project demonstration.

---

## ⚠️ Limitations

This is an **educational cybersecurity project**, not a production password-security service.

### Current limitations include:

- Pattern detection uses predefined educational rules.
- The common-password list is intentionally small and educational.
- The entropy value is theoretical.
- The score is a project-defined model.
- The analyzer does not provide exact password-cracking times.
- The application does not represent a complete authentication system.
- Production systems require additional controls such as HTTPS, secure session management, rate limiting, abuse protection, monitoring, and secure deployment.

A real authentication system should also use a well-established password hashing algorithm such as Argon2id, appropriate password policies, MFA, rate limiting, and other account-security controls.

---

## 🚀 Possible Future Improvements

Potential extensions include:

- Larger vetted common-password datasets
- More sophisticated password-pattern detection
- Password-manager integration
- Improved passphrase analysis
- More detailed policy configuration
- Additional security metrics
- Role-based administration for policy configuration
- Local-only bundled chart dependencies
- Security headers and production hardening
- More extensive automated test coverage
- Additional password-risk heuristics

---

## 🎓 Learning Outcomes

This project demonstrates practical understanding of:

- Defensive cybersecurity
- Password security
- Secure random generation
- Password policies
- Password hashing concepts
- Argon2id
- Entropy concepts
- Pattern detection
- Privacy-aware application design
- Secure data minimization
- Flask API development
- SQLite database design
- Frontend-backend communication
- Automated testing
- Security education and awareness

---

## 💼 Cybersecurity Relevance

The project connects directly to common defensive cybersecurity responsibilities involving:

- Identity and access security
- Credential security
- Authentication controls
- Security awareness
- Secure application development
- Data minimization
- Security monitoring
- Password-policy implementation

It demonstrates that cybersecurity is not limited to attack tools. **Preventing credential-related weaknesses and designing applications that minimize sensitive-data exposure are also important cybersecurity practices.**

---

## 📜 Disclaimer

This project is intended for **educational and defensive cybersecurity purposes only**.

Use synthetic demonstration passwords and information when testing the application.

Do not enter passwords belonging to other people or credentials that you do not want processed on your local machine.

The project does not attempt to crack, steal, recover, or test credentials against real accounts.

---
