# automation-essentials
Automation Essentials for Automation with Python

# 🧪 Selenium-Python POM Starter

This repository serves as a reusable foundation for automating web applications using **Selenium WebDriver**, **Python**, and the **Page Object Model (POM)** pattern.

> 💼 Designed as a personal testing briefcase to quickly bootstrap real-world automation projects.

---

## 📦 Tech Stack

- **Language**: Python 3.x
- **WebDriver**: Selenium
- **Test Runner**: Pytest
- **Pattern**: Page Object Model (POM)
- **Fixtures**: Pytest + conftest.py

---

## 🧱 Project Structure subject to changes

``` bash
├── pages/
│ ├── base_page.py
│ ├── login_page.py
│ ├── home_page.py
│ └── ...
├── tests/
│ ├── test_login.py
│ └── ...
├── conftest.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/eliasschepis/automation-essentials.git
cd automation-essentials
```

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run tests

pytest tests/

### 📄 Example Test

def test_login_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

### 📁 Pages
Each page follows the Page Object Model. Example:

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)

### ✅ TODOs (for future projects)
 Add Docker support

 Integrate Allure or HTML reporting

 Add GitHub Actions CI

 Include visual tests with Playwright

 Add REST API testing with requests or httpx

### 🧠 Notes
Use BasePage to reuse WebDriver and explicit waits across all page objects.

Group locators and actions cleanly to improve readability and scalability.

Build modular tests to support CI/CD pipelines and team collaboration.

### 📃 License

This project is open-source and free to use as a boilerplate. Personal adaptation encouraged.
