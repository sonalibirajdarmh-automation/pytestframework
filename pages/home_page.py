from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.elm_lnk_logout=(By.LINK_TEXT,"Logout")
        self.elm_lnk_newlead = (By.LINK_TEXT, "New Lead")
        self.elm_lnk_leads= (By.LINK_TEXT, "Leads")
        self.elm_lnk_NewAccount = (By.LINK_TEXT, "New Account")


    def VerifyLogout(self):
        return self.driver.find_element(*self.elm_lnk_logout).is_displayed()
    def clickLogout(self):
        self.driver.find_element(*self.elm_lnk_logout).click()


    def ClickNewLead(self):
        return self.driver.find_element(*self.elm_lnk_newlead).click()

    def ClickLeads(self):
        return self.driver.find_element(*self.elm_lnk_leads).click()

    def ClickNewAccount(self):
        return self.driver.find_element(*self.elm_lnk_NewAccount).click()
