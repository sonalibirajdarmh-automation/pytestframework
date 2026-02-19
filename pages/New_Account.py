from selenium.webdriver.common.by import By


class NewAccount:
    def __init__(self,driver):
        self.driver = driver
        self.elm_tb_accountname=(By.XPATH, "//input[@name='accountname']")
        self.elm_btn_save= (By.XPATH, "(//input[@value='  Save  '])[2]")
        #self.elm_lbl_text_Accountname = (By.XPATH, "//td[text()='Account Name:']/following::td[text()='Test_Vtiger']")

    def Create_account(self,Aname):
        self.Setaccountname(Aname)

    def Setaccountname(self,Aname):
        self.driver.find_element(*self.elm_tb_accountname).send_keys(Aname)

    def clickSave(self):
        self.driver.find_element(*self.elm_btn_save).click()

    #def verify_label_Accountname(self, Aname):
        #return self.driver.find_element(By.XPATH,
                                           # "//td[text()='Account Name:']/following::td[text()='" + Aname + "']").is_displayed()

