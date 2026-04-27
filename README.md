# Selenium SauceDemo Tests

## Overview
This project demonstrates automated UI testing using **Selenium WebDriver** with **PyTest**.  
It covers login scenarios (positive and negative) and a full end‑to‑end checkout flow on the [SauceDemo](https://www.saucedemo.com/) practice site.

The repo is structured using the **Page Object Model (POM)** for maintainability and includes reusable helpers in `utils/`.

---

## Features
- ✅ Positive login test (valid credentials)
- ❌ Negative login tests (invalid username, invalid password, both invalid)
- 🛒 End‑to‑end checkout flow (add to cart → checkout info → overview → finish → confirmation)
- 📂 Clean project structure with `pages/`, `tests/`, and `utils/`
- 🔄 Reusable driver utilities (explicit waits, helpers)

---

## Setup & Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/Yasteel7/Selenium_saucedemo_tests.git
   cd Selenium_saucedemo_tests

Install dependencies:
pip install -r requirements.txt

Run tests:
pytest -v

---

Tech Stack:

Python 3.14.3

Selenium WebDriver

PyTest

Page Object Model (POM) design pattern

---
