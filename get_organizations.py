from selenium import webdriver
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

############### 
# SET AMOUNT OF ENTRIES YOU WANT TO ADD 
entries = 207
# ADD TO THIS NUMBER EVER TIME YOU FINISH RUNNING THE PROGRAM (IF THE PAGE NUMBER WENT UP BY 1)
page_num = 1
###############
list_of_comapnies = pd.read_csv('Crunchbase_Research_Scripted.csv')

number_of_rows = len(list_of_comapnies.index)
print(list_of_comapnies)
print(number_of_rows)

# translate_table = str.maketrans({' ': '-', '.': '-'})
# for index, row in lon.iterrows():
#     name = row['Name']
#     name = name.translate(translate_table)
#     name = name.lower()
#     lon.at[index,'Name'] = name

web = webdriver.Chrome()
web.get('https://www.crunchbase.com')

###### LOGGING INTO CRUNCHBASE #####
time.sleep(8)
loginHeader = web.find_element_by_xpath('/html/body/chrome/div/app-header/div[1]/div[2]/div/anon-nav-row/nav-action-item[2]/nav-header-action-item/a')
loginHeader.click()

emailAddress = 'yearzerostudios@gmail.com'
emailField = web.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/mat-form-field[1]/div/div[1]/div/input')
emailField.send_keys(emailAddress)
time.sleep(1)

password = 'Yearzer0'
passwordField = web.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/mat-form-field[2]/div/div[1]/div/input')
passwordField.send_keys(password)
time.sleep(1)

loginButton = web.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/button')
loginButton.click()
time.sleep(1)

########## GETTING THE NEW COMPANIES #######
web.get(f'https://www.crunchbase.com/discover/organization.companies/7e8ad6c5d3d8f8af630a3abf1efb3d6b?pageId=1_a_7775a705-8556-4f3b-7743-946110a52111')
entries_added = 0
while entries > 0:
    time.sleep(3)
    for row in range(50):
        ClosingDate = WebDriverWait(web, 15).until(EC.visibility_of_element_located((By.XPATH, f"/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[6]/div/field-formatter/span"))).get_attribute('innerHTML')
        isAcquired = WebDriverWait(web, 15).until(EC.visibility_of_element_located((By.XPATH, f"/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[3]/div/field-formatter/enum-multi-formatter/span"))).get_attribute('innerHTML')
        print(f'VALUE OF isAcquired IS  :{isAcquired}')
        print(f'VALUE OF CLOSING DATE IS:{ClosingDate}')
        if ("—" in isAcquired):
            OrganizationName = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[2]/div/field-formatter/identifier-formatter/a/div/div').get_attribute('innerHTML')
            Founders = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[5]/div/field-formatter/identifier-multi-formatter/span').get_attribute('innerHTML')
            Founders = BeautifulSoup(Founders, "html.parser").get_text()
            FoundingDate = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[7]/div/field-formatter/span').get_attribute('innerHTML')
            # ClosingDate = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[6]/div/field-formatter/span').get_attribute('innerHTML')
            Industry = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[10]/div/field-formatter/identifier-multi-formatter/span').get_attribute('innerHTML')
            Industry = BeautifulSoup(Industry, "html.parser").get_text()
            Funding = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[14]/div/field-formatter/a').get_attribute('innerHTML')
            HQLocation = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[11]/div/field-formatter/identifier-multi-formatter/span').get_attribute('innerHTML')
            HQLocation = BeautifulSoup(HQLocation, "html.parser").get_text()
            Employees = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[4]/div/field-formatter').get_attribute('innerHTML')
            Employees = BeautifulSoup(Employees, "html.parser").get_text()
            AboutDescription = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[12]/div/field-formatter/span').get_attribute('innerHTML')
            Link = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[{row+1}]/grid-cell[2]/div/field-formatter/identifier-formatter/a').get_attribute('href')
            print(f"ORGANIZATION NAME: {OrganizationName}")
            print(f"FOUNDERS: {Founders}")
            print(f"FOUNDING DATE: {FoundingDate}")
            print(f"CLOSING DATE: {ClosingDate}")
            print(f"INDUSTRY: {Industry}")
            print(f"FUNDING: {Funding}")
            print(f"HQ LOCATION: {HQLocation}")
            print(f"EMPLOYEES: {Employees}")
            print(f"ABOUT/DESCRIPTION: {AboutDescription}")
            print(f"LINK: {Link}")
            new_row = {'Organization Name': OrganizationName, 'Founders': Founders, 'Founding Date': FoundingDate, 'Closing Date': ClosingDate, 'Industry': Industry, 'Funding': Funding, 'HQ Location': HQLocation, 'Employees': Employees, 'About/Description': AboutDescription, 'Slug': Link}
            list_of_comapnies = list_of_comapnies.append(new_row, ignore_index=True)
            print('\n\nNew row added to DataFrame\n--------------------------')
            print(list_of_comapnies)
            entries_added += 1
            entries -= 1
            print(f'VALUE OF ENTRIES: {entries}')
        if entries == 0:
            print(f'Finished! Total new entires added: {entries_added}')
            break
    if entries > 0:
        next_button = web.find_element_by_xpath(f'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[1]/div/results-info/h3/a[2]')
        next_button.click()

# print(list_of_comapnies) 
list_of_comapnies.to_csv('New_Crunchbase_Research.csv', encoding='utf-8')
