# 🚀 Python API Automation Framework

A **Hybrid Custom API Automation Framework** built using **Python** for robust, scalable, and maintainable API testing. This framework follows industry best practices with a clean folder structure, parallel execution, reporting, and data-driven testing.

![Framework Screenshot](https://github.com/user-attachments/assets/3c7d5fe5-207a-42e7-84fe-f4d53354d987)

---

## 👤 Author

**Prashant Kavinkar**

🔗 **LinkedIn**: [https://www.linkedin.com/in/prashant-kavinkar](https://www.linkedin.com/in/prashant-kavinkar)

📌 *QA Automation Engineer | API Automation | Python | PyTest*

---

## 📌 Key Highlights

* Hybrid and scalable API automation framework
* Clean and maintainable folder structure
* Data-driven testing support
* Parallel execution for faster test runs
* Multiple reporting options
* Easily extendable for new APIs

---

## 🛠 Tech Stack

* **Language**: Python 3.12
* **HTTP Client**: Requests
* **Test Framework**: PyTest
* **Reporting**:

  * Allure Report
  * PyTest HTML Report
* **Test Data Sources**:

  * CSV
  * Excel
  * JSON
* **Fake Data Generation**: Faker
* **Schema Validation**: jsonschema
* **Parallel Execution**: pytest-xdist

---

## 📂 Project Structure

```text
Python-API-Automation-Framework/
│
├── config/              # Environment & configuration files
├── data/                # Test data (CSV, Excel, JSON)
├── payloads/            # Request payloads
├── schemas/             # JSON schema validations
├── tests/               # Test cases
│   └── crud/             # CRUD API tests
├── utils/               # Utility helpers
├── reports/             # Test execution reports
├── requirements.txt     # Project dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd Python-API-Automation-Framework
```

### 2️⃣ Install Required Packages

```bash
pip install requests pytest pytest-html faker allure-pytest jsonschema
```

### 3️⃣ Install Parallel Execution Plugin

```bash
pip install pytest-xdist
```

---

## ▶️ Test Execution

### 🔹 Run Tests in Parallel

```bash
pytest -n auto
```

### 🔹 Run a Specific Test Case

```bash
pytest tests/tests/crud/test_create_booking.py
```

### 🔹 Run Tests with Allure Report

```bash
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s
```

### 🔹 Generate Allure Report

```bash
allure serve allure_result
```

---

## 📊 Reporting

* **Allure Report** – Rich and interactive test reports
* **PyTest HTML** – Lightweight HTML reporting

Reports help track:

* Test execution status
* Failure reasons
* Execution time
* Environment details

---

## ✅ Best Practices Followed

* Modular and reusable code
* Separation of test logic and test data
* Schema validation for API responses
* Logging and reporting support
* Parallel execution for CI/CD readiness

---

## 🤝 Contribution Guidelines

Contributions are welcome! 🚀

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Raise a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🌟 Support

If you find this project helpful:

* ⭐ Star the repository
* 🧩 Fork it
* 🔄 Share with the community

Happy Testing! 🎯
