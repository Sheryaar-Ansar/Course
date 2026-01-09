import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

# ===================== USER INPUT =====================
code = input("ENTER YOUR COMPANY CODE HERE:- ")
username = input("ENTER YOUR USERNAME HERE:- ")
fabric_entry = input("1 INVOICE ENTRY NUMBER:- ")
fabric_amount = input("TOTAL BILL AMOUNT OF 1:- ")
fancy_entry = input("2 INVOICE ENTRY NUMBER:- ")
fancy_amount = input("TOTAL BILL AMOUNT OF 2 :- ")
# mix_entry = input("3 INVOICE ENTRY NUMBER:- ")
# mix_amount = input("TOTAL BILL AMOUNT OF 3 :- ")
time_data = int(input("TIME GAP BETWEEN EACH ENTRY (seconds):- "))
number = int(input("NUMBER OF TIMES TO REGISTER ENTRIES:- "))

# ===================== EDGE HEADLESS SETUP =====================
service = Service(r"D:\msedgedriver.exe")
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-notifications")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = webdriver.Edge(service=service, options=options)
wait = WebDriverWait(driver, 60)  # increased wait for slow dropdowns
action = ActionChains(driver)

# ===================== HELPER FUNCTIONS =====================
def open_sales_invoice_headless():
    """Headless-safe navigation to SALES INVOICE page"""
    # Force open main menu
    driver.execute_script("""
        var menu = document.getElementById('LeftPanel_LeftPanelContent_Menu_DXI0_T');
        if (menu) { menu.click(); }
    """)
    time.sleep(1)

    # Force open submenu
    driver.execute_script("""
        var submenu = document.getElementById('LeftPanel_LeftPanelContent_Menu_DXI0i0_T');
        if (submenu) { submenu.click(); }
    """)
    time.sleep(1)

    # Click final link by innerText
    driver.execute_script("""
        var links = document.getElementsByTagName('a');
        for (var i = 0; i < links.length; i++) {
            if (links[i].innerText.trim() === 'SALES INVOICE (FBR INTEGRATED)') {
                links[i].click();
                break;
            }
        }
    """)
    time.sleep(2)

def safe_click(by, value, retries=4):
    for attempt in range(retries):
        try:
            elem = wait.until(EC.presence_of_element_located((by, value)))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
            wait.until(EC.element_to_be_clickable((by, value)))
            try:
                elem.click()
            except:
                driver.execute_script("arguments[0].click();", elem)
            return
        except (TimeoutException, StaleElementReferenceException):
            time.sleep(1)
    raise Exception(f"FAILED CLICK AFTER RETRIES: {value}")

def safe_send(by, value, text, retries=3):
    for _ in range(retries):
        try:
            elem = wait.until(EC.visibility_of_element_located((by, value)))
            elem.clear()
            time.sleep(0.5)
            elem.send_keys(text)
            return
        except (TimeoutException, StaleElementReferenceException):
            time.sleep(1)
    raise Exception(f"FAILED TO SEND KEYS: {value}")

def safe_double_click(by, value):
    elem = wait.until(EC.visibility_of_element_located((by, value)))
    action.double_click(elem).perform()

def handle_alert(action="accept", timeout=20):
    """
    Handles a browser alert.
    action: "accept" or "dismiss"
    """
    try:
        alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
        if action == "accept":
            alert.accept()
        elif action == "dismiss":
            alert.dismiss()
        time.sleep(1)  # give browser a moment to process
    except:
        pass


def select_dx_dropdown_item(item_text, timeout=140):
    """Select an item from DevExpress dropdown using parent tbody.
    If the item is not found, do nothing."""

    try:
        container = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBT"]/tbody')
            )
        )

        # Wait until rows appear
        WebDriverWait(driver, timeout).until(
            lambda d: len(container.find_elements(By.TAG_NAME, "tr")) > 0
        )

        rows = container.find_elements(By.TAG_NAME, "tr")

        # Track if we actually selected anything
        selected = False

        for row in rows:
            td = row.find_element(By.TAG_NAME, "td")
            cell_text = td.text.strip().replace("\n", " ").lower()  # clean text
            target_text = item_text.strip().lower()
            if target_text in cell_text:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", td)
                driver.execute_script("arguments[0].click();", td)
                selected = True
                break  # stop after selecting

        if not selected:
            print(f"⚠ Text '{item_text}' not found — skipping selection")

    except TimeoutException:
        print(f"⚠ Dropdown did not load in {timeout} seconds — skipping selection")



# ===================== LOGIN =====================
driver.get(f"http://5.223.43.152:{code}")
driver.maximize_window()

safe_send(By.ID, 'PageContent_FormLayout_UserNameTextBox_I', username)
safe_send(By.ID, 'PageContent_FormLayout_PasswordButtonEdit_I', "2580")
safe_send(By.ID, 'PageContent_FormLayout_CmbCompany_I', "SKF")
safe_click(By.ID, 'PageContent_FormLayout_SignInButton_CD')
time.sleep(2)
safe_click(By.ID, 'PageContent_FormLayout_SignInButton_CD')

# ===================== NAVIGATION =====================
# Replace these IDs with actual menu IDs if needed
# safe_click(By.ID, 'LeftPanel_LeftPanelContent_Menu_DXI0_T')
# safe_click(By.ID, 'LeftPanel_LeftPanelContent_Menu_DXI0i0_T')
# safe_click(By.LINK_TEXT, 'SALES INVOICE (FBR INTEGRATED)')
# if "--headless=new" in driver.capabilities.get("goog:chromeOptions", {}).get("args", []):
#     open_sales_invoice_headless()
# else:
#     safe_click(By.ID, 'LeftPanel_LeftPanelContent_Menu_DXI0_T')
#     safe_click(By.ID, 'LeftPanel_LeftPanelContent_Menu_DXI0i0_T')
#     safe_click(By.LINK_TEXT, 'SALES INVOICE (FBR INTEGRATED)')
open_sales_invoice_headless()


# ===================== MAIN LOOP =====================

def create_invoice(item_text, list_id, entry_no, amount, label):
    """Create one invoice entry"""
    safe_click(By.ID, "PageContent_GridView_DXCTMenu0_ITCNT1_NewInvoice_1_CD")
    time.sleep(3)  # wait for new invoice form

    safe_click(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_DropList_B-1Img")
    time.sleep(1)

    select_dx_dropdown_item(item_text)
    time.sleep(1)

    safe_double_click(By.ID, list_id)
    time.sleep(1)

    # # Click the target cell in invoice grid
    # cell = wait.until(EC.element_to_be_clickable((
    #     By.XPATH,
    #     "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]"
    # )))
    # cell.click()
    # time.sleep(2)
    # safe_send(By.ID,
    #           "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I",
    #           entry_no)
    # click the cell to activate editor
    cell = driver.find_element(By.XPATH, "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[7]")
    cell.click()
    time.sleep(2)  # wait for DevExpress editor to appear

    # send entry number
    entry_input = driver.find_element(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_DetailGrid_DXEditor6_I")
    entry_input.send_keys(fabric_entry)
    time.sleep(2)

    amount_box = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "/html/body/form/div[11]/table[2]/tbody/tr/td/div[4]/div/div/div[2]/div/table/tbody/tr/td/div/div/div/div/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/div/table[4]/tbody/tr[2]/td/table/tbody/tr/td/input"
    )))
    amount_box.click()
    time.sleep(0.5)
    amount_box.send_keys(amount)

    safe_click(By.ID, "PageContent_GridView_DXPEForm_efnew_tabs_StatusBarLayout_btnSave_CD")
    handle_alert(action="accept", timeout=10)
    # time.sleep(3)
    handle_alert(action="dismiss", timeout=30)
    print(f" '{label}' Invoice '{entry_no}' submitted successfully")
    time.sleep(time_data)

# ===================== REGISTER INVOICES =====================
for _ in range(number):
    # Fabric
    create_invoice(
        "Ladies Fabrics (Fancy) (5408)",
        "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI1T2",
        fabric_entry,
        fabric_amount,
        "FANCY"
    )

    # Fancy
    create_invoice(
        "LADIES FABRIC (5408)",
        "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI2T2",
        fancy_entry,
        fancy_amount,
        "FABRIC"
    )

    # # Mix
    # create_invoice(
    #     "LADIES Un-stitched suites (5 assorted colours & designs) (6204)",
    #     "PageContent_GridView_DXPEForm_efnew_tabs_DropList_DDD_lbAvailable_0_LBI0T2",
    #     mix_entry,
    #     mix_amount,
    #     "UNSTITCHED"
    # )

driver.quit()
