from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Arijit\Selenium\Webdrivers\chromedriver.exe")
driver.get("https://www.bestbuy.com/")
driver.maximize_window()

driver.implicitly_wait(10)

if driver.find_element_by_xpath("//button[@class='c-close-icon c-modal-close-icon']").is_displayed():
    print("Appeared!")
    driver.find_element_by_xpath("//button[@class='c-close-icon c-modal-close-icon']").click()

# click Account
driver.find_element_by_xpath("//span[@class='plButton-label v-ellipsis']").click()

# click Sign In
driver.find_element_by_link_text("Sign In").click()


driver.find_element_by_xpath("//span[@class='c-overlay-wrapper']").click()
infoMessage = driver.find_element_by_xpath("//div[@class='c-overlay right  ']/div[1]/div").text
expectedMessage = "We'll keep you signed in on this device. For your account's security, we'll still ask for your password if you're updating sensitive information. Use this option only on your personal computer or device."
assert infoMessage == expectedMessage
driver.find_element_by_xpath("//div[@class='c-overlay right  ']/button").click()
driver.find_element_by_xpath("//a[contains(text(),'Return to previous page')]").click()
print(driver.title)

# driver.find_element_by_xpath("//input[@type='email']").send_keys("arijit05saha@gmail.com")
# driver.find_element_by_xpath("//input[@type='password']").send_keys("Something@05")
# driver.find_element_by_xpath("//button[contains(text(),'Sign In')]").click()

#driver.close()