import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
website = "https://authorized-partner.vercel.app/"
driver.get(website)
driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[3]/header/div[1]/div/a[2]/button").click()

remember = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "remember"))
)
remember.click()
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/div[3]/a/button"))
)
continue_button.click()


First_name = "Anista"
Last_name = "Amatya"
Email_adress = "xudevu@fxzig.com"
Phone_number = "+9779842621622"
Password = "AnistaVirtTech!123"
confirm_password = Password

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "firstName"))
).send_keys(First_name)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "lastName"))
).send_keys(Last_name)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "email"))
).send_keys(Email_adress)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "phoneNumber"))
).send_keys(Phone_number)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "password"))
).send_keys(Password)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "confirmPassword"))
).send_keys(confirm_password)
next_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))
)
next_btn.click()

otp = input("Enter the 6-digit OTP sent to your email: ")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-input-otp="true"]'))
).send_keys(otp)
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Verify Code')]"))
).click()

#agencydetails
Agency_name = "Anista Amatya Agency"
Role = "Manager"
Agency_email = "Anista@anista.com"
Website = "anistaamatya.com"
Address = "Kathmandu, Nepal"
Region_of_Operation = "Canada"

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "agency_name"))
).send_keys(Agency_name)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "role_in_agency"))
).send_keys(Role)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "agency_email"))
).send_keys(Agency_email)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "agency_website"))
).send_keys(Website)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "agency_address"))
).send_keys(Address)


WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[role="combobox"]'))
).click()

canada_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[text()='Canada']"))
)
canada_option.click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))
).click()

#proffesional Experience
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='combobox' and .//text()[contains(.,'Experience')]]")
    )
).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[.='3 years']"))
).click()
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter an approximate number.']")
    )
).send_keys("120")
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[contains(@placeholder,'admissions to Canada')]")
    )
).send_keys("Undergraduate admissions to Canada")
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@type='number' and contains(@placeholder,'90%')]")
    )
).send_keys("95")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Career Counseling')]"))
).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Test Prepration')]"))
).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))
).click()

# Verification and Preferences
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "business_registration_number"))
).send_keys("12312313")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='combobox' and contains(.,'Preferred Countries')]")
    )
).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[.='Canada']"))
).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Colleges')]"))
).click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
).send_keys(r"C:\\Users\\UiN\Desktop\\Test\\logo.png")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))
).click()

print("Success")
time.sleep(10)
driver.quit()
