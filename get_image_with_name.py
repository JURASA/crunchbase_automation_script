from selenium import webdriver
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


lon = pd.read_csv('Names.csv')


print(lon)
translate_table = str.maketrans({' ': '-', '.': '-'})
for index, row in lon.iterrows():
    name = row['Name']
    name = name.translate(translate_table)
    name = name.lower()
    lon.at[index,'Name'] = name

web = webdriver.Chrome()
web.get('https://www.crunchbase.com')


time.sleep(5)
loginHeader = web.find_element_by_xpath('/html/body/chrome/div/app-header/div[1]/div[2]/div/anon-nav-row/nav-action-item[2]/nav-header-action-item/a')
loginHeader.click()



emailAddress = 'yearzerostudios@gmail.com'
emailField = web.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/mat-form-field[1]/div/div[1]/div/input')
emailField.send_keys(emailAddress)

password = 'Yearzer0'
passwordField = web.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/mat-form-field[2]/div/div[1]/div/input')
passwordField.send_keys(password)

loginButton = web.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/button')
loginButton.click()

for index, row in lon.iterrows():
    time.sleep(1)
    name = row['Name']
    web.get(f'https://www.crunchbase.com/organization/{name}')
    try:
        src = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/profile-header/div/header/div/div/div/div[1]/identifier-image/div/img"))).get_attribute("src")
        print(src)
        lon.at[index,'Links'] = src
    except TimeoutException:
        print(f"Skipped {name}")

print(lon) 
lon.to_csv('name_and_links.csv', encoding='utf-8')
