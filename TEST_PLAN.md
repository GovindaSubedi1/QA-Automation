# TEST PLAN – Playwright Automation Project

## 1. Project Overview

This test plan defines the scope, test scenarios, edge cases, and risks for automating the SauceDemo web application using Playwright with Python.

Target Application:
https://www.saucedemo.com

---

## 2. Scope

### In Scope

* Login functionality
* Product listing page
* Add to cart / Remove from cart
* Cart validation
* Checkout process
* Form validations
* Logout functionality
* UI navigation flows

### Out of Scope

* Performance testing
* Security penetration testing
* Database testing
* Mobile responsiveness testing

---

## 3. Test Scenarios (UI)

### Login Tests

1. Verify valid login with standard_user
2. Verify invalid login with wrong credentials
3. Verify login with empty username and password

### Product Tests

4. Verify product list is displayed after login
5. Verify product sorting (A-Z / Z-A)
6. Verify product details page opens correctly

### Cart Tests

7. Add product to cart and verify cart badge count
8. Remove product from cart and verify update

### Checkout Tests

9. Complete checkout with valid user details
10. Verify checkout form validation for empty fields

---

## 4. Edge Cases

* Login with locked_out_user
* Adding same product multiple times
* Clicking checkout without products
* Empty form submission during checkout
* Rapid click on Add/Remove buttons

---

## 5. Negative Test Cases

* Invalid username/password login
* Empty login submission
* Checkout without filling mandatory fields

---

## 6. Risks

* Application downtime or instability
* UI element changes affecting locators
* Network latency affecting test execution
* Rate limiting or session timeout issues

---

## 7. Test Data

* standard_user / secret_sauce (valid login)
* invalid_user / invalid_pass (negative test)
* locked_out_user (restricted user)

---

## 8. Automation Strategy

* Framework: Playwright + Pytest
* Design Pattern: Page Object Model (POM)
* Reporting: HTML report + screenshots on failure
* Execution: Parallel + headless/headed modes
