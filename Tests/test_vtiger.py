import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.Login_page import LoginPage
from pages.home_page import HomePage
from pages.lead_page import Leads
from pages.New_Account import NewAccount


def test_verify_title_TC01(driver):
    #driver=launchApp()
    lp=LoginPage(driver)
    istitle=lp.verify_title()
    assert "vtiger CRM - Commercial Open Source CRM" in driver.title



def test_verify_logo_TC02(driver):
    #driver=launchApp()
    lp=LoginPage(driver)
    islogo=lp.verify_logo()
    assert islogo==True


def test_Valid_login_TC03(driver):
    #driver=launchApp()
    lp=LoginPage(driver)
    lp.login(uid="admin", pwd="admin")
    hp=HomePage(driver)
    assert hp.VerifyLogout()==True


def test_Invalid_logo_TC04(driver):
    #driver=launchApp()
    lp=LoginPage(driver)
    lp.login(uid="admin", pwd="admin123")
    assert lp.verify_msg()==True

#create lead test-->create lead test ,edit lead test,delete lead test,search lead test
def test_createLead_with_mandatory_fields(driver):
    #driver=launchApp()
    lp=LoginPage(driver)
    lp.login(uid="admin", pwd="admin")
    hp=HomePage(driver)
    hp.ClickNewLead()
    ldp=Leads(driver)
    ldp.create_lead("Modi","BJP")
    assert ldp.verify_label_lastname("Modi") == True
    assert ldp.verify_label_company("BJP") == True
    hp.ClickLeads()
    ldp.search_lead("Modi","BJP")
    time.sleep(5)
    #assert ldp.verify_Search_lastname("Gandhi") == True
   # assert ldp.verify_Search_company("congress") == True
    #time.sleep(5)
    hp.clickLogout()



def test_CreateNewAccount(driver):
    lp=LoginPage(driver)
    lp.login(uid="admin", pwd="admin")
    hp=HomePage(driver)
    hp.ClickNewAccount()
    na=NewAccount(driver)
    na.Create_account("Test_vtiger")
    #assert na.verify_label_Accountname("Test_vtiger") == True
    time.sleep(5)
    hp.clickLogout()







