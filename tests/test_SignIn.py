from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestSignIn(BaseClass):

    signInPage = ""

    def test_keepSignInfo(self):
        if self.getPageTitle() != "Sign In to Best Buy":
            signInPage = self.openSignInPage()

        signInPage.getKeepSignedInfo().click()
        infoMessage = signInPage.getKeepSignedInfoText().text
        print(infoMessage)

        expectedMessage = "We'll keep you signed in on this device. For your account's security, we'll still ask for your password if you're updating sensitive information. Use this option only on your personal computer or device."
        assert infoMessage == expectedMessage

        signInPage.getKeepSignedInfoTextCloseButton().click()

    def test_signIn(self):
        if self.getPageTitle() != "Sign In to Best Buy":
            signInPage = self.openSignInPage()

        signInPage.getEmail().send_keys("arijit05saha@gmail.com")
        signInPage.getPassword().send_keys("Something@05")
        signInPage.getSignIn().click()

    def test_returnToPrevPage(self):
        if self.getPageTitle() != "Sign In to Best Buy":
            signInPage = self.openSignInPage()
        signInPage.getReturnToPrevPage().click()
        pageTitle = self.getPageTitle()
        assert pageTitle == "Best Buy | Official Online Store | Shop Now & Save"

