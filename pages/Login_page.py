from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.elm_img_logo=(By.XPATH, "//img[@src='include/images/login_left.gif']")
        self.elm_tb_username=(By.NAME, "user_name")
        self.elm_tb_password=(By.NAME, "user_password")
        self.elm_btn_login= (By.NAME, "Login")
        self.elm_msg_error=(By.XPATH,"//*[contains(text(),'You must specify a valid username and password.')]")


    def verify_title(self):
        return  self.driver.title

    def verify_logo(self):
        return self.driver.find_element(*self.elm_img_logo).is_displayed()

    def login(self,uid,pwd):
        self.setUsername(uid)
        self.setPassword(pwd)
        self.click_login()
        print("Login Successful")
        print("hello git")

    def setUsername(self,uid):
        self.driver.find_element(*self.elm_tb_username).clear()
        self.driver.find_element(*self.elm_tb_username).send_keys(uid)

    def setPassword(self,pwd):
        self.driver.find_element(*self.elm_tb_password).clear()
        self.driver.find_element(*self.elm_tb_password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.elm_btn_login).click()

    def verify_msg(self):
        return self.driver.find_element(*self.elm_msg_error).is_displayed()

