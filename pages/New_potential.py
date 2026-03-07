
from selenium.webdriver.common.by import By

class NewPotential:
    def __init__(self,driver):
        self.driver = driver
        self.elm_tb_potentialname=(By.XPATH, "//input[@name='potentialname']")
        self.elm_tb_change=(By.XPATH, "//input[@value='Change']")
        self.elm_tb_Aname=(By.XPATH, "///a[text()='vtiger']")
        self.elm_btn_Save=(By.XPATH, "//input[@value='Save']")




    def createPotential(self,Pname):
        self.setpotentialname(Pname)
        self.setAccountname()
        self.click_Save()

    def setpotentialname(self,Pname):
        self.driver.find_element(*self.elm_tb_potentialname).send_keys(Pname)

    def setAccountname(self):
        self.driver.find_element(*self.elm_tb_change).click()
        self.driver.find_element(*self.elm_tb_Aname).click()


    def click_Save(self):
        self.driver.find_element(*self.elm_btn_Save).click()


