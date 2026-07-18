<div align="center">

# 🚀 Selenium Pytest Automation Framework

### Production-Ready UI Test Automation Framework using Selenium, Python & Pytest

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reports-orange?style=for-the-badge)](https://allurereport.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](LICENSE)

A scalable, production-ready UI Automation Framework built using **Python**, **Selenium**, **Pytest**, and the **Page Object Model (POM)**.

Designed with clean architecture, maintainability, reusable components, data-driven testing, reporting, logging, and CI/CD readiness.

</div>

---

# 📖 Overview

This framework demonstrates industry-standard automation practices that are commonly used in enterprise QA teams.

It provides a modular architecture for writing maintainable UI automation tests while supporting:

- Cross-browser execution
- Headless execution
- Page Object Model
- Data-driven testing
- Allure Reporting
- HTML Reports
- Screenshot capture
- Logging
- Configuration management
- CI/CD integration

---

# ✨ Features

| Feature | Status |
|----------|:------:|
| Selenium WebDriver | ✅ |
| Pytest Framework | ✅ |
| Page Object Model (POM) | ✅ |
| Browser Factory Pattern | ✅ |
| Chrome Support | ✅ |
| Microsoft Edge Support | ✅ |
| Headless Mode | ✅ |
| Explicit Waits | ✅ |
| Implicit Waits | ✅ |
| Loguru Logging | ✅ |
| CSV Data Driven Testing | ✅ |
| Excel Data Driven Testing | ✅ |
| HTML Reports | ✅ |
| Allure Reports | ✅ |
| Screenshot on Failure | ✅ |
| Environment Configuration | ✅ |
| GitHub Actions Ready | ✅ |
| Docker Ready | ✅ |

---

# 🏗 Architecture

```
                 Test Cases
                      │
                      ▼
              Page Object Model
                      │
                      ▼
                 Base Page
                      │
                      ▼
               Browser Factory
                      │
                      ▼
              Selenium WebDriver
                      │
                      ▼
                 Web Browser
```

---

# 📂 Project Structure

```
selenium-pytest-automation-framework/

│
├── .github/
│   └── workflows/
│       └── selenium-tests.yml
│
├── app/
│   ├── config/
│   ├── core/
│   ├── pages/
│   ├── services/
│   └── utils/
│
├── docker/
├── docs/
├── logs/
├── reports/
├── screenshots/
├── test_data/
│   ├── login_data.csv
│   └── login_data.xlsx
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_logout.py
│   ├── test_login_csv.py
│   └── test_login_excel.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# 🛠 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python 3.12+ |
| Automation | Selenium |
| Test Runner | Pytest |
| Reporting | Allure, HTML Report |
| Logging | Loguru |
| Data Driven | CSV, Excel |
| Configuration | Pydantic |
| Version Control | Git & GitHub |

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/ShreyashMahalle75/selenium-pytest-automation-framework.git
```

Move into the project

```bash
cd selenium-pytest-automation-framework
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running Tests

Run all tests

```bash
pytest
```

Verbose mode

```bash
pytest -v
```

Chrome

```bash
pytest --browser chrome
```

Edge

```bash
pytest --browser edge
```

Chrome Headless

```bash
pytest --headless
```

Edge Headless

```bash
pytest --browser edge --headless
```

Parallel Execution

```bash
pytest -n auto
```

---

# 📊 Reports

## HTML Report

Generate

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Allure Report

Generate

```bash
pytest --alluredir=allure-results
```

Open

```bash
allure serve allure-results
```

---

# 📸 Screenshot Capture

Whenever a test fails the framework automatically:

- Captures screenshot
- Saves inside `screenshots/`
- Attaches screenshot to Allure Report

---

# 📑 Data Driven Testing

Supports:

- CSV
- Excel (.xlsx)

Example:

```
test_data/

login_data.csv
login_data.xlsx
```

---

# 🧩 Design Patterns Used

- Page Object Model (POM)
- Browser Factory Pattern
- Service Layer
- Base Page Abstraction
- Configuration Pattern

---

# 🚀 CI/CD

GitHub Actions automatically:

- Install dependencies
- Execute all tests
- Validate pull requests

Workflow

```
Push
     │
     ▼

GitHub Actions

     │

Install Dependencies

     │

Run Pytest

     │

Generate Reports

     │

Build Status
```

---

# 🐳 Docker Support

Build

```bash
docker build -t selenium-framework .
```

Run

```bash
docker run selenium-framework
```

---

# 📈 Future Improvements

- Jenkins Integration
- BrowserStack Integration
- Playwright Version
- API Automation
- Performance Testing
- AI-assisted Test Generation

---

# 📷 Project Preview

You can add screenshots here.

```
docs/images/

allure-dashboard.png

html-report.png

github-actions.png
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 👨‍💻 Author

## **Shreyash Mahalle**

**AI & Data Science Engineer**

GitHub

https://github.com/ShreyashMahalle75

LinkedIn

https://www.linkedin.com/in/shreyash-mahalle/

---

# ⭐ Show Your Support

If you found this project useful,

⭐ Star the repository

🍴 Fork it

📢 Share it

---

<div align="center">

### Built with ❤️ using Python, Selenium & Pytest

</div>
