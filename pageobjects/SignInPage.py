from selenium.webdriver.common.by import By


class SignInPage:
    email = (By.XPATH, "//input[@type='email']")
    password = (By.XPATH, "//input[@type='password']")
    signIn = (By.XPATH, "//button[contains(text(),'Sign In')]")
    keepSignedInfo = (By.XPATH, "//span[@class='c-overlay-wrapper']")
    keepSignedInfoText = (By.XPATH, "//div[@class='c-overlay right  ']/div[1]/div")
    keepSignedInfoTextCloseButton = (By.XPATH, "//div[@class='c-overlay right  ']/button")
    returnToPrevPage = (By.XPATH, "//a[contains(text(),'Return to previous page')]")

    def __init__(self, driver):
        self.driver = driver


    def getEmail(self):
        return self.driver.find_element(*SignInPage.email)

    def getPassword(self):
        return self.driver.find_element(*SignInPage.password)

    def getSignIn(self):
        return self.driver.find_element(*SignInPage.signIn)

    def getKeepSignedInfo(self):
        return self.driver.find_element(*SignInPage.keepSignedInfo)

    def getKeepSignedInfoText(self):
        return self.driver.find_element(*SignInPage.keepSignedInfoText)

    def getKeepSignedInfoTextCloseButton(self):
        return self.driver.find_element(*SignInPage.keepSignedInfoTextCloseButton)

    def getReturnToPrevPage(self):
        return self.driver.find_element(*SignInPage.returnToPrevPage)
