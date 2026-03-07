from selenium.webdriver.common.by import By

class NewTicket:
    def __init__(self,driver):
        self.driver = driver
        self.elm_tb_title=(By.XPATH, "//textarea[@name='ticket_title']")
        self.elm_btn_Save=(By.XPATH, "(//input[@type='submit'])[2]")

        #verifytitle
        self.elm_tb_stitlename=(By.XPATH, "//td[text()='Title:']/following::td[text()='testing']")




    def createticket(self,title):
        self.setticketname(title)
        self.click_Save()

    def setticketname(self,title):
        self.driver.find_element(*self.elm_tb_title).send_keys(title)

    def click_Save(self):
        self.driver.find_element(*self.elm_btn_Save).click()


###########Verify ticket#############


    def verify_ticket(self, stitle):
       return self.driver.find_element(By.XPATH,"//td[text()='Title:']/following::td[text()='" + stitle+ "']").is_displayed()