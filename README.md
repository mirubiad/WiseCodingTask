# Automated Test for Wise Platform

## Overview
This project contains an automated test script for the Wise platform using Python, Selenium, and pytest. The script performs key actions such as logging in as a tutor, navigating to a classroom, scheduling a session, and verifying session details.

## Technologies Used
- Python
- Selenium WebDriver
- pytest
- allure (for reporting)

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Google Chrome or Microsoft Edge
- ChromeDriver or Edge WebDriver (compatible with your browser version)
- Required Python packages (see below for installation)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/mirubiad/WiseCodingTask.git
   cd WiseCodingTask
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Test
To execute the test, run the following command:
```sh
pytest test_wise_app.py --alluredir=reports/
```

To generate an Allure report:
```sh
allure serve reports/
```

## Test Scenario
### Steps performed in the test:
1. **Login as Tutor**
   - Visit `https://staging-web.wise.live`
   - Enter phone number `+911111100000`
   - Enter OTP `0000`
   - Assert login success
2. **Navigate to Classroom**
   - Click on "Group courses" tab
   - Select "Classroom for Automated testing"
   - Verify that the classroom is opened
3. **Schedule a Session**
   - Click on "Live Sessions" tab
   - Click "Schedule Sessions"
   - Click "Add session" and set time to `10:00 PM`
   - Click "Create"
4. **Verify the Session**
   - Ensure session appears on the timeline
   - Verify session details (instructor name, session name, session time, upcoming status)

## Notes
- This script runs on **Microsoft Edge** by default but can be modified to use Chrome.
- The OTP is hardcoded for testing purposes.
- If the test fails, check the web element locators and update accordingly.


