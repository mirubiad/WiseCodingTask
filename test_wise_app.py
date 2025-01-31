import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType

@allure.title("Wise-Web|| Verify that a new session is successfully added")
@allure.description("Login as a tutor and add a new session at 10PM")
@allure.label("Owner", "Mir_Ubaid")
def test_schedule_session(driver):
    wait = WebDriverWait(driver, timeout=10)

# Step 1: Perform login as a tutor
    # Visit https://staging-web.wise.live
    driver.get("https://staging-web.wise.live")

    # Proceed to login using phone number
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Continue with Mobile')]")))
    login_with_phone = driver.find_element(By.XPATH, "//span[contains(.,'Continue with Mobile')]")
    login_with_phone.click()

    # Enter the phone number (+911111100000) and OTP (0000)
    phone_number_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Phone number']")
    phone_number_field.send_keys("1111100000")

    get_otp_btn = driver.find_element(By.XPATH, "//span[contains(., 'Get OTP')]")
    get_otp_btn.click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Enter OTP']"))
    )

    otp_fields = driver.find_elements(
        By.CSS_SELECTOR, "input.otp-field-box--0, input.otp-field-box--1, input.otp-field-box--2, "
                         "input.otp-field-box--3")  # Find all OTP input fields

    otp = "0000"

    for i in range(4):  # Enter OTP digits into respective fields
        otp_fields[i].send_keys(otp[i])

    verify_btn = driver.find_element(By.XPATH, "//span[contains(., 'Verify')]")
    verify_btn.click()

    # Assert that the institute name “Testing Institute” is showing up
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Testing Institute')]")))
    institute_name = driver.find_element(By.XPATH, "//span[contains(.,'Testing Institute')]")
    assert institute_name.text == "Testing Institute"

    allure.attach(driver.get_screenshot_as_png(), name="Institute Name", attachment_type=AttachmentType.PNG)

# Step 2: Go to the classroom
    # Click on “Group courses” tab
    group_courses_tab = driver.find_element(By.XPATH, "//span[normalize-space()='Group courses']")
    group_courses_tab.click()

    # Click and choose “Classroom for Automated testing” classroom
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Classroom for Automated testing']")))
    classroom_for_automated_testing = driver.find_element(By.XPATH,
                                                          "//a[normalize-space()='Classroom for Automated testing']")
    classroom_for_automated_testing.click()

    # Assert that classroom is opened successfully
    wait.until(EC.title_is("Classroom for Automated testing - WISE"))
    assert driver.title == "Classroom for Automated testing - WISE"

    allure.attach(driver.get_screenshot_as_png(), name="Automated testing classroom", attachment_type=AttachmentType.PNG)

# Step 3: Schedule a session
    # Click on “Live sessions” tab and click on “Schedule sessions
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Live Sessions']")))
    live_sessions_tab = driver.find_element(By.XPATH, "//a[normalize-space()='Live Sessions']")
    live_sessions_tab.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Schedule Sessions')]")))
    schedule_session_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Schedule Sessions')]")
    schedule_session_btn.click()

    # On the scheduling UI, on the left side, click on “Add session”
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add session']")))
    add_session_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Add session']")
    add_session_btn.click()

    # and choose the time to schedule a session for today at 10pm
    wait.until(EC.visibility_of_element_located((By.ID, "input-652")))
    session_time = driver.find_element(By.ID, "input-652")
    session_time.clear()
    session_time.send_keys("10:00")

    am_pm_indicator = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='text--16']")))
    if am_pm_indicator.text == "PM":
        # PM is already selected, no need to click
        pass
    else:
        # AM is selected, click to toggle to PM
        am_pm_indicator.click()

    # Click to “create”
    create_session_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create']"))
    )
    create_session_button.click()

# Step 4: Assert the session
    # On the classroom home screen assert that sessions card is shown on the timeline
    session_card = wait.until(
        EC.visibility_of_element_located((By.XPATH,"//div[contains(@class, 'session-container')]//div[contains(@class, 'session')]//div[contains(text(), 'Fri, 3:00 pm - 4:00 pm')]"))
    )
    assert session_card.is_displayed()

    allure.attach(driver.get_screenshot_as_png(), name="Session details", attachment_type=AttachmentType.PNG)

    # Assert the session details such as instructor name, session name, session
    # time, upcoming status, etc
    instructor_name = driver.find_element(By.XPATH, "//div[contains(@class, 'teachers-card')]")
    session_date = driver.find_element(By.XPATH, "//div[normalize-space()='31 Jan 25']")
    session_time = driver.find_element(By.XPATH, "//div[normalize-space()='10:00 PM']")

    assert "Wise Tester" in instructor_name.text, "Instructor name not visible"
    assert "31 Jan 25" in session_date.text, "Incorrect session date"
    assert "10:00 PM" in session_time.text, "Incorrect session time"

    driver.quit()
