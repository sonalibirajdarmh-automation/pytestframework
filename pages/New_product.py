from selenium.webdriver.common.by import By

class NewProduct:
    def __init__(self, driver):
        self.driver = driver
        self.elm_tb_pname=(By.XPATH,"//input[@name='productname']")
        self.elm_btn_save=(By.XPATH,"(//input[@type='submit'])[2]")


    def CreateNewProduct(self,pname):
        self.setproductname(pname)
        self.click_Save()

    def setproductname(self, pname):
        self.driver.find_element(*self.elm_tb_pname).send_keys(pname)

    def click_Save(self):
        self.driver.find_element(*self.elm_btn_save).click()
