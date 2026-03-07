from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.elm_lnk_logout=(By.LINK_TEXT,"Logout")
        self.elm_lnk_newlead = (By.LINK_TEXT, "New Lead")
        self.elm_lnk_leads= (By.LINK_TEXT, "Leads")
        self.elm_lnk_NewAccount = (By.LINK_TEXT, "New Account")
        self.elm_lnk_NewPotential = (By.LINK_TEXT, "New Potential")
        self.elm_lnk_NewTicket = (By.LINK_TEXT, "New Ticket")
        self.elm_lnk_NewProduct = (By.LINK_TEXT, "New Product")




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

    def ClickNewPotential(self):
        return self.driver.find_element(*self.elm_lnk_NewPotential).click()

    def ClickNewTicket(self):
        return self.driver.find_element(*self.elm_lnk_NewTicket).click()

    def ClickNewproduct(self):
        return self.driver.find_element(*self.elm_lnk_NewProduct).click()
