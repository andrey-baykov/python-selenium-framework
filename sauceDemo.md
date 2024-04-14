# sauceDemo framework
## What in this framework?
- Page Object Model
- Selenium WebDriver
- Allure Report
- Logger module
- Jama mockup
- API mockup

## How to install?
Clone project from GitHub
```bash
git clone TODO
```
Install all required packages
```bash

pip install -r requirements.txt
``` 

## How to run?
### With allure report
1. Run all test cases with allure report
```bash
pytest --alluredir=report
```
2. Generate report
```bash
allure serve report
```
### Without allure report
Run all tests
```bash
pytest -v
```

or run specific test:
```bash
pytest -v -k test_standard_user_can_complete_purchase
```
```bash
pytest -v -k test_locked_out_user_cannot_login
```
```bash
pytest -v -k test_problem_user_encounters_issues
```
