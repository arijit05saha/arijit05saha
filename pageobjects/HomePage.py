from selenium.webdriver.common.by import By

from pageobjects.SignInPage import SignInPage


class HomePage:

    account = (By.XPATH, "//span[@class='plButton-label v-ellipsis']")
    signIn = (By.LINK_TEXT, "Sign In")

    def __init__(self, driver):
        self.driver = driver

        # close the pop-up for Sing Up at the initial launch of home page
        self.driver.implicitly_wait(10)
        if self.driver.find_element_by_xpath("//button[@class='c-close-icon c-modal-close-icon']").is_displayed():
            self.driver.find_element_by_xpath("//button[@class='c-close-icon c-modal-close-icon']").click()

    def getAccount(self):
        return self.driver.find_element(*HomePage.account)

    def getSignIn(self):
        self.driver.find_element(*HomePage.signIn).click()
        signInPage = SignInPage(self.driver)
        return signInPage


