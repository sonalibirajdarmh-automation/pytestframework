from selenium.webdriver.common.by import By


class Leads:
    def __init__(self, driver):
        self.driver = driver
        self.elm_tb_lastname = (By.NAME, "lastname")
        self.elm_tb_company = (By.NAME, "company")
        self.elm_btn_save = (By.NAME, "button")
        self.elm_lbl_text_lastname = (By.XPATH, "//td[text()='Last Name:']/following::td[text()='Modi']")
        self.elm_lbl_text_company = (By.XPATH, "//td[text()='Company:']/following::td[text()='BJP']")
        self.elm_tb_slastname=(By.XPATH,"(//input[@name='lastname'])[2]")
        self.elm_tb_scompany =(By.XPATH,"(//input[@name='company'])[2]")
        self.elm_btn_search = (By.XPATH, "(//input[@type='submit'])[2]")
        # self.elm_lbl_text_slastname=(By.XPATH,"//td[text()='Gandhi']")
        # self.elm_lbl_text_scompany(By.XPATH,"//td[text()='Congress']")

        print("In develope branch")

    def create_lead(self, lname, company):
        self.setlastname(lname)
        self.setCompany(company)
        self.clickSave()


    def setlastname(self, lname):
        self.driver.find_element(*self.elm_tb_lastname).send_keys(lname)

    def setCompany(self, company):
        self.driver.find_element(*self.elm_tb_company).send_keys(company)

    def clickSave(self):
        self.driver.find_element(*self.elm_btn_save).click()

    def verify_label_lastname(self, lname):
        return self.driver.find_element(By.XPATH,
                                        "//td[text()='Last Name:']/following::td[text()='" + lname + "']").is_displayed()

    def verify_label_company(self, company):
        return self.driver.find_element(By.XPATH,
                                        "//td[text()='Company:']/following::td[text()='" + company + "']").is_displayed()
    def search_lead(self, slname, scompany):
        self.searchlastname(slname)
        self.searchCompany(scompany)
        self.clickSearch()


    def searchlastname(self, slname):
        self.driver.find_element(*self.elm_tb_slastname).send_keys(slname)

    def searchCompany(self, scompany):
        self.driver.find_element(*self.elm_tb_scompany).send_keys(scompany)

    def clickSearch(self):
        self.driver.find_element(*self.elm_btn_search).click()

    # def verify_Search_lastname(self, slname):
    #     return self.driver.find_element(By.XPATH,"//a[@href='Name']/descendant::td[text()='" + slname + "']").is_displayed()
    #
    # def verify_Search_company(self, scompany):
    #     return self.driver.find_element(By.XPATH,
    #                                  "/td[text()='Company']/descendant::td[text()='"+scompany+"']").is_displayed()







