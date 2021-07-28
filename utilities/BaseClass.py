import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass():
    def verifyLinkPresence(self, text):
        waitElement = WebDriverWait(self.driver, 7)
        waitElement.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def openHomePage(self):
        homepage = HomePage(self.driver)
        return homepage

    def openSignInPage(self):
        homepage = self.openHomePage()
        homepage.getAccount().click()
        signInPage = homepage.getSignIn()
        return signInPage

    def getPageTitle(self):
        return self.driver.title

    def closePage(self):
        self.driver.close()