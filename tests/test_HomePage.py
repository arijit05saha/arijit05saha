from selenium import webdriver

from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_signIn(self):
        homepage = HomePage(self.driver)
        homepage.getAccount().click()
        signInPage = homepage.getSignIn()
