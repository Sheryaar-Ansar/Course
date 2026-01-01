import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
username=input("ENTER YOUR USERNAME HERE:-")
#password=input("ENTER YOUR PASSWORD HERE:-")
# company=input("ENTER YOUR COMPANY HERE:-")
date_input=input("Enter the Date of the Day:- ")
fabric_entry=input("FANCY INVOICE ENTRY NUMBER:- ")
fabric_amount=input("TOTAL BILL AMOUNT OF FANCY:-")
fabric1_entry=input("FABRIC INVOICE ENTRY NUMBER:- ")
fabric1_amount=input("TOTAL BILL AMOUNT OF FABRIC :-")
fancy_entry=input("FANCY 1 INVOICE ENTRY NUMBER:- ")
fancy_amount=input("TOTAL BILL AMOUNT OF FANCY 1 :-")
fabric2_entry=input("FABRIC 1 INVOICE ENTRY NUMBER:- ")
fabric2_amount=input("TOTAL BILL AMOUNT OF FABRIC 1:-")
##unstitched_entry=input("UNSTITCHED INVOICE ENTRY NUMBER:- ")
##unstitched_amount=input("TOTAL BILL AMOUNT OF UNSTITCHED:-")
##garment_entry=input("garment ITEM INVOICE ENTRY NUMBER:-")
##garment_amount=input("TOTAL BILL AMOUNT OF garment ITEM:-")
##sfabric_entry=input("S_FABRIC INVOICE ENTRY NUMBER:- ")
##sfabric_amount=input("TOTAL BILL AMOUNT OF S_FABRIC:-")
##sfancy_entry=input("S_FANCY INVOICE ENTRY NUMBER:- ")
##sfancy_amount=input("TOTAL BILL AMOUNT OF S_FANCY:-")
##sunstitched_entry=input("S_UNSTITCHED INVOICE ENTRY NUMBER:- ")
##sunstitched_amount=input("TOTAL BILL AMOUNT OF S_UNSTITCHED:-")
time_data=int(input("TIME GAP BETWEEN EACH ENTRY:-"))
number=int(input("1 LIKHNE SE 3 ENTRIES REGISTER HONGI:-"))


#def headless_chrome():
  #  ser_obj=Service(executable_path='D:\chromedriver.exe')
 #   ops=webdriver.ChromeOptions()
    #ops.headless=True
   # driver=webdriver.Chrome(service=ser_obj, options=ops)
 ##   return driver
#driver=headless_chrome()

ser_obj=Service(executable_path='D:\msedgedriver.exe')
driver=webdriver.Edge(service=ser_obj)



driver.get("http://142.132.145.204:2112/")
driver.maximize_window()
action=ActionChains(driver)
driver.find_element(By.ID, 'PageContent_FormLayout_UserNameTextBox_I').send_keys(username)
driver.find_element(By.ID, 'PageContent_FormLayout_PasswordButtonEdit_I').send_keys("2580")
time.sleep(2)
driver.find_element(By.ID, 'PageContent_FormLayout_SignInButton_CD').click()
time.sleep(2)
driver.find_element(By.ID, 'PageContent_FormLayout_SignInButton_CD').click()
time.sleep(5)

driver.find_element(By.ID, 'LeftPanel_LeftPanelContent_Menu_DXI0_T').click()
time.sleep(2)
driver.find_element(By.ID, 'LeftPanel_LeftPanelContent_Menu_DXI0i0_T').click()
time.sleep(1)
driver.find_element(By.LINK_TEXT, 'SALES INVOICE (FBR INTEGRATED)').click()
time.sleep(3)
for r in range(number):
    time.sleep(5)
    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
    time.sleep(15)
    date = driver.find_element(By.NAME, "ctl00$PageContent$GridView$DXPEForm$efnew$TC$tabs$formLayout$txtTransactionDate")
    date.click()
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    date.send_keys(date_input)
    date.send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
    time.sleep(27)
    fabric=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI0T2") #1
    time.sleep(3)
    action.double_click(fabric).perform()
    time.sleep(4)
    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
    time.sleep(2)
    element.click()
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(fabric_entry)
    time.sleep(2)
    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
    box.click()

    time.sleep(1)
    box.send_keys(fabric_amount)
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
    time.sleep(3)
    try:
        alert1=driver.switch_to.alert
        alert1.accept()
    except:
        pass
    time.sleep(18)
    try:
        alert2=driver.switch_to.alert
        alert2.dismiss()
    except:
        pass
    try:
        print("Embroided (2) invoice successfully submit")
    except:
        pass

    time.sleep(time_data) #the time period you want to stop the invoice

    time.sleep(15)
    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
    time.sleep(15)
    date = driver.find_element(By.NAME, "ctl00$PageContent$GridView$DXPEForm$efnew$TC$tabs$formLayout$txtTransactionDate")
    date.click()
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    date.send_keys(date_input)
    date.send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
    time.sleep(27)
    fabric1=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI0T2") #1
    time.sleep(3)
    action.double_click(fabric1).perform()
    time.sleep(4)
    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
    time.sleep(2)
    element.click()
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(fabric1_entry)
    time.sleep(2)
    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
    box.click()

    time.sleep(1)
    box.send_keys(fabric1_amount)
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
    time.sleep(3)
    try:
        alert3=driver.switch_to.alert
        alert3.accept()
    except:
        pass
    time.sleep(18)
    try:
        alert4=driver.switch_to.alert
        alert4.dismiss()
    except:
        pass
    try:
        print("Embroided (2) invoice successfully submit")
    except:
        pass

    time.sleep(time_data) #the time period you want to stop the invoice

    time.sleep(15)
    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
    time.sleep(15)
    date = driver.find_element(By.NAME, "ctl00$PageContent$GridView$DXPEForm$efnew$TC$tabs$formLayout$txtTransactionDate")
    date.click()
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    date.send_keys(date_input)
    date.send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
    time.sleep(27)
    fabric2=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI0T2") #1
    time.sleep(3)
    action.double_click(fabric2).perform()
    time.sleep(4)
    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
    time.sleep(2)
    element.click()
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(fancy_entry)
    time.sleep(2)
    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
    box.click()

    time.sleep(1)
    box.send_keys(fancy_amount)
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
    time.sleep(3)
    try:
        alert5=driver.switch_to.alert
        alert5.accept()
    except:
        pass
    time.sleep(18)
    try:
        alert6=driver.switch_to.alert
        alert6.dismiss()
    except:
        pass
    try:
        print("Embroided (2) invoice successfully submit")
    except:
        pass

    time.sleep(time_data) #the time period you want to stop the invoice

    time.sleep(15)
    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
    time.sleep(15)
    date = driver.find_element(By.NAME, "ctl00$PageContent$GridView$DXPEForm$efnew$TC$tabs$formLayout$txtTransactionDate")
    date.click()
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    date.send_keys(date_input)
    date.send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
    time.sleep(27)
    fabric3=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI0T2") #1
    time.sleep(3)
    action.double_click(fabric3).perform()
    time.sleep(4)
    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
    time.sleep(2)
    element.click()
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(fabric2_entry)
    time.sleep(2)
    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
    box.click()

    time.sleep(1)
    box.send_keys(fabric2_amount)
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
    time.sleep(3)
    try:
        alert7=driver.switch_to.alert
        alert7.accept()
    except:
        pass
    time.sleep(18)
    try:
        alert8=driver.switch_to.alert
        alert8.dismiss()
    except:
        pass
    try:
        print("Embroided (2) invoice successfully submit")
    except:
        pass

    time.sleep(time_data) #the time period you want to stop the invoice




driver.close()
