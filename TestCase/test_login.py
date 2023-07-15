import pytest
from selenium import webdriver
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

from PageObjects.LoginPage import LoginPage


class Test_001_login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_HomePageTitle(self, setup):
        self.logger.info("**************** Test_001_login ***********")
        self.logger.info("**************** Veryfying home page title ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** Home page title is passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("**************** Home page title is failed ***********")
            assert False

    def test_Login(self, setup):
        self.logger.info("**************** Veryfying login page ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************** Login page is passed ***********")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_Login.png")
            self.driver.close()
            self.logger.error("**************** Login page is failed ***********")
            assert False

    #print(os.getcwd())




