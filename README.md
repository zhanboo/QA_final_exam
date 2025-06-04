# QA_final_exam


# QA_FINALS - Python Project

This project includes two things:
1. A Python function to check if someone is old enough to drive.
2. A website login test using Selenium.

---

## 🧾 Files in this folder

- `main_file.py`: Has the `can_drive(age)` function.
- `driving_test.py`: Unit tests to check if the function works.
- `login_test.py`: A script that tries logging into a website using Selenium.

---

## 🛠️ How to Use

### 1. Run the unit test
To check if the `can_drive()` function works:
```bash
python driving_test.py
```

### 2. Run the login test
To run the browser test:
```bash
python login_test.py
```

> Make sure you have Google Chrome and ChromeDriver installed.

If you don’t have Selenium yet:
```bash
pip install selenium
```

---

## ✅ What You’ll See

**Unit test output:**
```
.....
OK
```

**Login test output:**
```
✅ SUCCESS: Login worked for test1
❌ FAIL: Login failed for test1
```
