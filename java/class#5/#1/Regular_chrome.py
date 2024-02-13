import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
username=input("ENTER YOUR USERNAME HERE:-")
#password=input("ENTER YOUR PASSWORD HERE:-")
# company=input("ENTER YOUR COMPANY HERE:-")
fabric_entry=input("FABRIC INVOICE ENTRY NUMBER:- ")
fabric_amount=input("TOTAL BILL AMOUNT OF FABRIC:-")
fancy_entry=input("Fancy INVOICE ENTRY NUMBER:- ")
fancy_amount=input("TOTAL BILL AMOUNT OF Fancy :-")
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



driver.get("http://103.76.29.122:8089/")
driver.maximize_window()
action=ActionChains(driver)
driver.find_element(By.ID, 'PageContent_FormLayout_UserNameTextBox_I').send_keys(username)
driver.find_element(By.ID, 'PageContent_FormLayout_PasswordButtonEdit_I').send_keys("2580")
driver.find_element(By.ID, 'PageContent_FormLayout_CmbCompany_I').send_keys("SKF")
time.sleep(2)
driver.find_element(By.ID, 'PageContent_FormLayout_SignInButton_CD').click()

time.sleep(5)

driver.find_element(By.ID, 'LeftPanel_LeftPanelContent_Menu_DXI3_T').click()
time.sleep(2)
driver.find_element(By.ID, 'LeftPanel_LeftPanelContent_Menu_DXI3i0_P').click()
time.sleep(1)
driver.find_element(By.LINK_TEXT, 'SALES INVOICE (FBR INTEGRATED)').click()
time.sleep(3)
for r in range(number):
    time.sleep(5)
    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
    time.sleep(10)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
    time.sleep(10)
    fabric=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI2T2")
    time.sleep(5)
    action.double_click(fabric).perform()
    time.sleep(4)
    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
    time.sleep(2)
    element.click()
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(fabric_entry)
    time.sleep(2)
    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
    box.click()

    time.sleep(1)
    box.send_keys(fabric_amount)
    time.sleep(3)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
    time.sleep(5)
    try:
        alert1=driver.switch_to.alert
        alert1.accept()
    except:
        pass
    time.sleep(10)
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


#    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
#    time.sleep(10)
#    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
#    time.sleep(10)
###    search=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBFE_I")
###    search.click()
###    search.send_keys("acid")
###    time.sleep(3)
#    
#    garment=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI5T2")
#    time.sleep(5)
#    action.double_click(garment).perform()
#    time.sleep(4)
#    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
#    time.sleep(2)
#    element.click()
#    time.sleep(2)
#    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(garment_entry)
#    time.sleep(2)
#    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
#    box.click()
#
#    time.sleep(1)
#    box.send_keys(garment_amount)
#    time.sleep(2)
#    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
#    time.sleep(5)
#    try:
#        alert1=driver.switch_to.alert
#        alert1.accept()
#    except:
#        pass
#    time.sleep(12)
#    try:
#        alert2=driver.switch_to.alert
#        alert2.dismiss()
#    except:
#        pass
#    try:
#        print("MIX ITEM invoice successfully submit")
#    except:
#        pass
#
#    time.sleep(time_data) #the time period you want to stop the invoice


    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
    time.sleep(10)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
    time.sleep(10)
    fancy=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI1T2")
    time.sleep(8)
    action.double_click(fancy).perform()
    time.sleep(3)
    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
    time.sleep(2)
    element.click()
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(fancy_entry)
    time.sleep(2)
    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
    box.click()

    time.sleep(1)
    box.send_keys(fancy_amount)
    time.sleep(2)
    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
    time.sleep(5)
    try:
        alert1=driver.switch_to.alert
        alert1.accept()
    except:
        pass
    time.sleep(10)
    try:
        alert2=driver.switch_to.alert
        alert2.dismiss()
    except:
        pass
    try:
        print("Embroided (3) invoice successfully submit")
    except:
        pass


    time.sleep(time_data) #the time periodbr you want to stop the invoice


##    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
##    time.sleep(18)
##    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
##    time.sleep(10)
##    unstitched=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI0T2")
##    time.sleep(5)
##    action.double_click(unstitched).perform()
##    time.sleep(4)
##    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
##    time.sleep(2)
##    element.click()
##    time.sleep(2)
##    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(unstitched_entry)
##    time.sleep(2)
##    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
##    box.click()
##
##    time.sleep(1)
##    box.send_keys(unstitched_amount)
##    time.sleep(2)
##    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
##    time.sleep(10)
##    try:
##        alert1=driver.switch_to.alert
##        alert1.accept()
##    except:
##        pass
##    time.sleep(18)
##    try:
##        alert2=driver.switch_to.alert
##        alert2.dismiss()
##    except:
##        pass
##    try:
##        print("Unstitched invoice successfully submit")
##    except:
##        pass
##
##    time.sleep(time_data) #the time period you want to stop the invoice
    
    
##    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
##    time.sleep(10)
##    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
##    time.sleep(18)
##    sfabric=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI5T2")
##    time.sleep(5)
##    action.double_click(sfabric).perform()
##    time.sleep(4)
##    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
##    time.sleep(2)
##    element.click()
##    time.sleep(2)
##    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(sfabric_entry)
##    time.sleep(2)
##    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
##    box.click()
##
##    time.sleep(1)
##    box.send_keys(sfabric_amount)
##    time.sleep(3)
##    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
##    time.sleep(5)
##    try:
##        alert1=driver.switch_to.alert
##        alert1.accept()
##    except:
##        pass
##    time.sleep(18)
##    try:
##        alert2=driver.switch_to.alert
##        alert2.dismiss()
##    except:
##        pass
##    try:
##        print("S_Fabric invoice successfully submit")
##    except:
##        pass
##
##    time.sleep(time_data) #the time period you want to stop the invoice
##
##    
##    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
##    time.sleep(10)
##    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
##    time.sleep(18)
##    sfancy=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI4T2")
##    time.sleep(5)
##    action.double_click(sfancy).perform()
##    time.sleep(4)
##    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
##    time.sleep(2)
##    element.click()
##    time.sleep(2)
##    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(sfancy_entry)
##    time.sleep(2)
##    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
##    box.click()
##
##    time.sleep(1)
##    box.send_keys(sfancy_amount)
##    time.sleep(3)
##    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
##    time.sleep(5)
##    try:
##        alert1=driver.switch_to.alert
##        alert1.accept()
##    except:
##        pass
##    time.sleep(18)
##    try:
##        alert2=driver.switch_to.alert
##        alert2.dismiss()
##    except:
##        pass
##    try:
##        print("S_Fancy invoice successfully submit")
##    except:
##        pass
##
##    time.sleep(time_data) #the time period you want to stop the invoice

    
##    driver.find_element(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD").click()
##    time.sleep(10)
##    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img"))).click()
##    time.sleep(18)
##    sunstitched=driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI3T2")
##    time.sleep(5)
##    action.double_click(sunstitched).perform()
##    time.sleep(4)
##    element=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
##    time.sleep(2)
##    element.click()
##    time.sleep(2)
##    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I").send_keys(sunstitched_entry)
##    time.sleep(2)
##    box=driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[6]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input")
##    box.click()
##
##    time.sleep(1)
##    box.send_keys(sunstitched_amount)
##    time.sleep(3)
##    driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD").click()
##    time.sleep(5)
##    try:
##        alert1=driver.switch_to.alert
##        alert1.accept()
##    except:
##        pass
##    time.sleep(18)
##    try:
##        alert2=driver.switch_to.alert
##        alert2.dismiss()
##    except:
##        pass
##    try:
##        print("S_Unstitched invoice successfully submit")
##    except:
##        pass
##
##    time.sleep(time_data) #the time period you want to stop the invoice

driver.close()
